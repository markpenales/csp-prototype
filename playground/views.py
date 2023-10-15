from django.shortcuts import render
from django.http import HttpResponse
from playground.constraint_satisfaction_problem.implementation import SchedulingProblem
from playground.forms import CreateScheduleForm

from playground.models import Course, Program, Schedule, Year, Section


# Create your views here.
def hello(request) -> HttpResponse:
    program = Program.objects.all()

    return render(request, "index.html", {"programs": program})


def year(request, program) -> HttpResponse:
    year = Year.objects.all()
    return render(request, "year.html", {"years": year, "program": program})


def section(request, program, year) -> HttpResponse:
    sections = Section.objects.filter(program=program, year=year).all()

    return render(
        request,
        "section.html",
        {"program": program, "year": year, "sections": sections},
    )


def section_schedule(request, id):
    schedules = Schedule.objects.filter(section=id).all()

    return render(request, "schedules.html", {"schedules": schedules, "id": id})


def create_section_schedule(request, id):
    section = Section.objects.get(id=id)
    courses = Course.objects.filter(program=section.program, year=section.year).all()

    if request.method == "POST":
        form = CreateScheduleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["course"])
            SchedulingProblem(form.cleaned_data["course"], section).solve()

    return render(request, "create_schedule.html", {"courses": courses})
