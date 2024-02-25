from django.urls import path

from . import views

urlpatterns = [
    path("sections/", views.get_sections, name="get_sections"),
    path("programs/", views.hello, name="programs"),
    path("programs/<program>", views.year, name="year"),
    path("programs/<program>/<year>", views.section, name="section"),
    path("schedule/section/<id>", views.section_schedule, name="schedule"),
    path("schedule/create/<id>", views.create_section_schedule, name="create_schedule"),
    path("schedule/save", views.save_section_schedule, name="save"),
]
