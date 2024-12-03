from django.urls import path

from cats.views import SpyCatSalaryUpdateView, SpyCatListView, SpyCatDetailView

urlpatterns = [
    path(
        "<int:pk>/update-salary/",
        SpyCatSalaryUpdateView.as_view(),
        name="spycat-update-salary",
    ),
    path("", SpyCatListView.as_view(), name="spycat-list"),
    path("<int:pk>/", SpyCatDetailView.as_view(), name="spycat-detail"),
]

app_name = "cats"
