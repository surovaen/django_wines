from rest_framework.pagination import PageNumberPagination


class WineResultPagination(PageNumberPagination):
    """Класс пагинации и лимита выборки вин."""

    page_size = 100
    page_size_query_param = 'limit'
    page_size_query_description = 'Количество результатов на странице'
    page_query_param = 'page'
    page_query_description = 'Номер страницы'
    max_page_size = 1000
