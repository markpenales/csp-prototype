from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from playground.constraint_satisfaction_problem.implementation import SchedulingProblem
from playground.forms import CreateScheduleForm, SaveScheduleForm
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from playground.models import Course, Instructor, Laboratory, Program, Schedule, Year, Section, Day
from pprint import pprint
import json
from django.db.models import F


# Create your views here.
def hello(request) -> HttpResponse:
    program = Program.objects.all()
    year = Year.objects.all()

    return render(request, "index.html", {"programs": program, "years": year})

def get_sections(request):
    program_id = request.GET.get('program_id')
    year_id = request.GET.get('year_id')

    sections = Section.objects.filter(program_id=program_id, year_id=year_id).annotate(name=F('section_name__name')).values('id', 'name')
    sections = list(sections)
    return JsonResponse({'sections': sections})

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
    schedules = Schedule.objects.filter(section=id).prefetch_related('section', 'course', 'day', 'instructor', 'laboratory').all()

    return render(request, "schedules.html", {"schedules": schedules, "id": id})


def create_section_schedule(request, id):
    section = Section.objects.get(id=id)
    schedules = Schedule.objects.filter(section=section).all()
    courses = Course.objects.filter(program=section.program, year=section.year).all().exclude(id__in=[schedule.course.id for schedule in schedules])

    if request.method == "POST":
        form = CreateScheduleForm(request.POST)
        if form.is_valid():
            solutions = SchedulingProblem(form.cleaned_data["course"], section).solve()
            instructors = [{'instructor': solution.get('instructors').name, 'timeslot': solution.get('timeslot')} for solution in solutions]
            laboratories = list(set(solution.get('laboratory').name for solution in solutions))
            # for solution in solutions:
            #     solution['laboratory'] = model_to_dict(solution['laboratory'])
            #     solution['instructors'] = model_to_dict(solution['instructors'])
            # return JsonResponse(solutions, safe=False)
            instructor_set = {}
            for instructor in instructors:
                name = instructor['instructor']
                time = instructor['timeslot']
                if name not in instructor_set:
                    instructor_set[name] = [time]
                else:
                    if time not in instructor_set[name]:
                        instructor_set[name].append(time)
            days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            # Define a function to convert time to a sortable value
            def time_to_sortable_value(time_str):
                time_obj = datetime.strptime(time_str, '%I:%M %p')
                return time_obj.time()

            return render(request, "select_schedule.html", {"instructors": instructor_set, "laboratories": laboratories, "section": section.id, "course": form.cleaned_data["course"]})
            
            

    return render(request, "create_schedule.html", {"courses": courses})

def save_section_schedule(request):
    if request.method == "POST":
        form = SaveScheduleForm(request.POST)
        if form.is_valid():
            lab = Laboratory.objects.filter(name=form.cleaned_data['lab']).first()
            prof = Instructor.objects.filter(name=form.cleaned_data['prof']).first()
            time = form.cleaned_data['time']
            section = Section.objects.filter(id=form.cleaned_data['section']).first()
            course = Course.objects.filter(name=form.cleaned_data['course']).first()
            
            
            Schedule(
                section=section,
                course=course,
                day=Day.objects.filter(name=time.split(' ')[0]).first(),
                instructor=prof,
                laboratory=lab,
                time_start=time,
                time_end=get_time_end(time, course.units)
            ).save()
            
            
            
            return redirect('programs')
        

        else:
            print(f"Error {form.errors}")
            
from datetime import datetime, timedelta

def get_time_end(time_start, units):
    # Split the input time string
    time_arr = time_start.split(' ')
    day = time_arr.pop(0)
    time_end = ' '.join(time_arr)

    # Parse the time string into a datetime object
    start_time = datetime.strptime(time_end, "%I:%M %p")

    # Add units to the time
    end_time = start_time + timedelta(hours=units)

    # Format the result as a string
    time_end_str = end_time.strftime("%I:%M %p")
    
    # Combine day and time to get the final result
    result = f"{day} {time_end_str}"
    return result
