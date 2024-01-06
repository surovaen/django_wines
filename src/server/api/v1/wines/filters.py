from django.contrib.postgres.search import SearchQuery, TrigramSimilarity
from django.db.models import Q, QuerySet
from django_filters import rest_framework as filters

from server.wines.models import Wine


class WineFilter(filters.FilterSet):
    """Класс-фильтр по винам."""

    full_search = filters.CharFilter(
        label='Поиск по наименованию и описанию вина',
        method='full_search_filter',
    )
    bottling_date_from = filters.DateFilter(
        field_name='bottling_date',
        label='Дата розлива от',
        lookup_expr='gte',
    )
    bottling_date_to = filters.DateFilter(
        field_name='bottling_date',
        label='Дата розлива до',
        lookup_expr='lte',
    )

    class Meta:
        model = Wine
        fields = ['full_search', 'bottling_date']

    def full_search_filter(self, queryset: QuerySet, name: str, value: str) -> QuerySet:
        """Метод полнотекстового поиска по наименованию и описанию вина."""
        search_qs = queryset.annotate(
            similarity=TrigramSimilarity('name', value) + TrigramSimilarity('description', value),
        ).filter(
            Q(name_vector=SearchQuery(value)) | Q(description_vector=SearchQuery(value)) | Q(similarity__gte=0.1),
        )

        return search_qs
