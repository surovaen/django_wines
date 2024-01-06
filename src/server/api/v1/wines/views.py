from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from server.api.v1.wines.base.pagination import WineResultPagination
from server.api.v1.wines.filters import WineFilter
from server.api.v1.wines.serializers import WineSerializer
from server.wines.models import Wine


class WineView(ListAPIView):
    """Вью отображения списка вин и маркетов, в которых они находятся."""

    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WineFilter
    permission_classes = (IsAuthenticated,)
    pagination_class = WineResultPagination
