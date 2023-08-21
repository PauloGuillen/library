from rest_framework.filters import BaseFilterBackend
from django.db.models import Q


class BookFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filters = Q()

        if title := request.GET.get('title'):
            filters &= Q(title__icontains=title)

        if edition := request.GET.get('edition'):
            filters &= Q(edition__icontains=edition)

        if publication_year := request.GET.get('publication_year'):
            filters &= Q(publication_year=publication_year)

        if author_id := request.GET.get('author'):
            filters &= Q(authors=author_id)

        if author_name := request.GET.get('author_name'):
            filters &= Q(authors__name__icontains=author_name)

        return queryset.filter(filters)
