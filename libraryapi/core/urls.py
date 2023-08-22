from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path('author-test3/', views.AuthorList.as_view(), name='list-author'),
    path('author/', views.AuthorList.as_view(), name='list-author'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='detail-author'),
    path('book/', views.BookList.as_view(), name='list-book'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='detail-book'),
]
