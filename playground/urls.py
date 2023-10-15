from django.urls import path

from . import views

urlpatterns = [
    path("programs/", views.hello),
    path("programs/<program>", views.year, name="year"),
    path("programs/<program>/<year>", views.section, name="section"),
    path("schedule/section/<id>", views.section_schedule, name="schedule"),
    path("schedule/create/<id>", views.create_section_schedule, name="create_schedule"),
]
