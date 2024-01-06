from django.urls import path

from server.api.v1.wines.views import WineView


urlpatterns = [
    path('wines/', WineView.as_view()),
]
