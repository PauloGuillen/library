from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializers, BookSerializers
from .filters import BookFilterBackend


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

    def get_queryset(self):
        queryset = super().get_queryset()

        if name := self.request.GET.get('name'):
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [BookFilterBackend]
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
