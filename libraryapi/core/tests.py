import pytest
from http import HTTPStatus
from libraryapi.core.models import Author, Book

CT_JSON = 'application/json'
pytestmark = pytest.mark.django_db


@pytest.fixture
def author1(db):
    author1 = Author.objects.create(name='Brian K. Jones')
    return author1


@pytest.fixture
def book1(db, author1):
    author2 = Author.objects.create(name='David Beazley')
    book1 = Book.objects.create(
        title='Python Cookbook: Recipes for Mastering Python 3',
        edition='3rd',
        publication_year=2013,
    )
    book1.authors.add(author1)
    book1.authors.add(author2)

    return book1


def test_list_all_author(client):
    Author.objects.bulk_create(Author(name=f'Author {i:02}') for i in range(1, 75))

    response = client.get('/api/author/?page=2')
    assert response.status_code == HTTPStatus.OK
    assert [r['name'] for r in response.json()['results']] == [f'Author {i:02}' for i in range(26, 51)]


def test_search_author_by_name(client):
    author = Author.objects.create(name='Chetan Giridhar')
    response = client.get('/api/author/?name=Giridhar')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['results'] == [author.to_dict()]


def test_search_author_by_name_without_match(client):
    Author.objects.create(name='Chetan Giridhar')
    response = client.get('/api/author/?name=Mueller')

    assert response.json()['results'] == []


def test_create_author(client):
    data = {
        'name': 'David Beazley'
    }
    response = client.post('/api/author/', data=data, content_type=CT_JSON)

    assert response.status_code == HTTPStatus.CREATED

    author = Author.objects.first()
    assert response.json() == author.to_dict()


def test_read_author(client, author1):
    response = client.get(f'/api/author/{author1.id}/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == author1.to_dict()


def test_read_non_existing_author(client, author1):
    response = client.get('/api/author/999/')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_author(client, author1):
    data = {
        'id': author1.id,
        'name': author1.name + ' Alterado'
    }
    response = client.put(f'/api/author/{author1.id}/', data=data, content_type=CT_JSON)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == data
    author1.refresh_from_db()
    assert author1.to_dict() == data


def test_put_non_existing_author(client):
    response = client.put('/api/author/999/', data={}, content_type=CT_JSON)

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_author(client, author1):
    response = client.delete(f'/api/author/{author1.id}/')

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert not Author.objects.filter(pk=author1.id).exists()


def test_delete_non_existing_author(client, author1):
    response = client.delete('/api/author/999/')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_list_all_book(client):
    Book.objects.bulk_create(Book(
            title=f'Title {i:02}',
            edition='1rd',
            publication_year=2013
        ) for i in range(1, 75)
    )
    response = client.get('/api/book/?page=2')

    assert response.status_code == HTTPStatus.OK
    assert [r['title'] for r in response.json()['results']] == [f'Title {i:02}' for i in range(26, 51)]


def test_filter_book_by_title(client, book1):
    response = client.get(f'/api/book/?title={book1.title}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['results'] == [book1.to_dict()]


def test_filter_book_by_title_without_match(client, book1):
    response = client.get('/api/book/?title=Harry Poter')
    assert response.json()['results'] == []


def test_filter_book_by_edition(client, book1):
    response = client.get(f'/api/book/?edition={book1.edition}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['results'] == [book1.to_dict()]


def test_filter_book_by_edition_without_match(client, book1):
    response = client.get('/api/book/?edition=999')
    assert response.json()['results'] == []


def test_filter_book_by_publication_year(client, book1):
    response = client.get(f'/api/book/?publication_year={book1.publication_year}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['results'] == [book1.to_dict()]


def test_filter_book_by_publication_year_without_match(client, book1):
    response = client.get('/api/book/?publication_year=2099')
    assert response.json()['results'] == []


def test_filter_book_by_author(client, book1):
    author = Author.objects.create(name='Osvaldo Santana Neto')
    book1.authors.add(author)

    response = client.get(f'/api/book/?author={author.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['results'] == [book1.to_dict()]


def test_filter_book_by_author_without_match(client, book1):
    response = client.get('/api/book/?author=999')
    assert response.json()['results'] == []


def test_filter_book_by_author_name(client, book1):
    author = Author.objects.create(name='Osvaldo Santana Neto')
    book1.authors.add(author)

    response = client.get(f'/api/book/?author_name={author.name}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['results'] == [book1.to_dict()]


def test_filter_book_by_author_name_without_match(client, book1):
    response = client.get('/api/book/?author_name=J. K. Rowling')
    assert response.json()['results'] == []


def test_create_book(client, author1):
    author2 = Author.objects.create(name='David Beazley ')
    data = {
        'title': 'Python Cookbook: Recipes for Mastering Python 3',
        'edition': '3rd',
        'publication_year': 2013,
        'authors': [author1.id, author2.id]
    }

    response = client.post('/api/book/', data=data, content_type=CT_JSON)

    assert response.status_code == HTTPStatus.CREATED
    book = Book.objects.first()
    assert response.json() == book.to_dict()


def test_read_book(client, book1):
    response = client.get(f'/api/book/{book1.id}/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == book1.to_dict()


def test_read_non_existing_book(client, book1):
    response = client.get('/api/book/999/')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_book(client, book1):
    data = {
        'id': book1.id,
        'title': book1.title + '  *** alterado ***',
        'edition': book1.edition,
        'publication_year': book1.publication_year + 1,
        'authors': list(book1.authors.values_list('id', flat=True))
    }

    response = client.put(f'/api/book/{book1.id}/', data=data, content_type=CT_JSON)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == data
    book1.refresh_from_db()
    assert book1.to_dict() == data


def test_update_non_existing_book(client, book1):
    response = client.put('/api/book/999/', data={}, content_type=CT_JSON)

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_book(client, book1):
    response = client.delete(f'/api/book/{book1.id}/')

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert not Book.objects.filter(pk=book1.id).exists()


def test_delete_non_existing_book(client, book1):
    response = client.delete('/api/book/999/')

    assert response.status_code == HTTPStatus.NOT_FOUND
