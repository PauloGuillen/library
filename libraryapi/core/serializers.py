from rest_framework import serializers
from .models import Author, Book


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
