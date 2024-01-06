from django.urls import include, path

from server.api.v1.auth import urls as auth_urls
from server.api.v1.wines import urls as wines_urls


urlpatterns = [
    path('auth/', include(auth_urls)),
    path('wines/', include(wines_urls)),
]
