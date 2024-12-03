from django.urls import path, include

urlpatterns = [
    path("api/spy-cats/", include("cats.urls")),
    path("api/missions/", include("missions.urls")),
]
