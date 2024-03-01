from django.urls import path

from . import views

app_name = "issues"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:issue_id>/", views.detail, name="detail"),
    path("<int:issue_id>/comment/", views.comment, name="comment"),
    path("<int:issue_id>/complete/", views.complete, name="complete"),
]