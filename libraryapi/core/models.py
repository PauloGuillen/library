from django.db import models
import uuid


def pk_uuid():
    return int(str(uuid.uuid4())[-12:], 16)


class Author(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False, default=pk_uuid)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Book(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False, default=pk_uuid)
    title = models.CharField(max_length=200)
    edition = models.CharField(max_length=20)
    publication_year = models.SmallIntegerField()
    authors = models.ManyToManyField(Author)

    class Meta:
        ordering = ['title',]

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'edition': self.edition,
            'publication_year': self.publication_year,
            'authors': list(self.authors.values_list('id', flat=True))
        }
