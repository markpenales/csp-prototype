from constraint import *

from playground.models import Instructor
from playground.models import Laboratory
from playground.models import Schedule

from datetime import datetime


class SchedulingProblem:
    def __init__(
        self,
        course,
        section,
        instructor=None,
        laboratory=None,
        time=None,
        day=None,
    ):
        self.problem = Problem(BacktrackingSolver())
        self.course = course
        self.section = section

        # These constraints are hard constraints if they are defined
        self.laboratory = laboratory
        self.time = time
        self.day = day
        self.instructor = instructor

        self.timeslots = [
            "Monday 7:00 am",
            "Monday 8:00 am",
            "Monday 9:00 am",
            "Monday 10:00 am",
            "Monday 11:00 am",
            "Monday 12:00 pm",
            "Monday 1:00 pm",
            "Monday 2:00 pm",
            "Monday 3:00 pm",
            "Monday 4:00 pm",
            "Monday 5:00 pm",
            "Monday 6:00 pm",
            "Monday 7:00 pm",
            "Tuesday 7:00 am",
            "Tuesday 8:00 am",
            "Tuesday 9:00 am",
            "Tuesday 10:00 am",
            "Tuesday 11:00 am",
            "Tuesday 12:00 pm",
            "Tuesday 1:00 pm",
            "Tuesday 2:00 pm",
            "Tuesday 3:00 pm",
            "Tuesday 4:00 pm",
            "Tuesday 5:00 pm",
            "Tuesday 6:00 pm",
            "Tuesday 7:00 pm",
            "Wednesday 7:00 am",
            "Wednesday 8:00 am",
            "Wednesday 9:00 am",
            "Wednesday 10:00 am",
            "Wednesday 11:00 am",
            "Wednesday 12:00 pm",
            "Wednesday 1:00 pm",
            "Wednesday 2:00 pm",
            "Wednesday 3:00 pm",
            "Wednesday 4:00 pm",
            "Wednesday 5:00 pm",
            "Wednesday 6:00 pm",
            "Wednesday 7:00 pm",
            "Thursday 7:00 am",
            "Thursday 8:00 am",
            "Thursday 9:00 am",
            "Thursday 10:00 am",
            "Thursday 11:00 am",
            "Thursday 12:00 pm",
            "Thursday 1:00 pm",
            "Thursday 2:00 pm",
            "Thursday 3:00 pm",
            "Thursday 4:00 pm",
            "Thursday 5:00 pm",
            "Thursday 6:00 pm",
            "Thursday 7:00 pm",
            "Friday 7:00 am",
            "Friday 8:00 am",
            "Friday 9:00 am",
            "Friday 10:00 am",
            "Friday 11:00 am",
            "Friday 12:00 pm",
            "Friday 1:00 pm",
            "Friday 2:00 pm",
            "Friday 3:00 pm",
            "Friday 4:00 pm",
            "Friday 5:00 pm",
            "Friday 6:00 pm",
            "Friday 7:00 pm",
            "Saturday 7:00 am",
            "Saturday 8:00 am",
            "Saturday 9:00 am",
            "Saturday 10:00 am",
            "Saturday 11:00 am",
            "Saturday 12:00 pm",
            "Saturday 1:00 pm",
            "Saturday 2:00 pm",
            "Saturday 3:00 pm",
            "Saturday 4:00 pm",
            "Saturday 5:00 pm",
            "Saturday 6:00 pm",
            "Saturday 7:00 pm",
        ]

    def solve(self):
        labs = Laboratory.objects.all()
        instructors = Instructor.objects.all()

        self.problem.addVariable("laboratory", labs)
        self.problem.addVariable("timeslot", self.timeslots)
        self.problem.addVariable("instructors", instructors)

        self.problem.addConstraint(self.laboratory_constraint, ["laboratory"])
        self.problem.addConstraint(self.time_constraint, ["timeslot"])
        self.problem.addConstraint(self.instructors_constraint, ["instructors"])

        solutions = self.problem.getSolutions()
        if len(solutions) == 0:
            print("No solutions")
            self.problem.reset()
            self.problem.addVariable("timeslot", self.timeslots)
            self.problem.addVariable("laboratory", labs)
            self.problem.addVariable("instructors", instructors)
            self.problem.addConstraint(self.instructors_constraint, ["instructors"])
            self.problem.addConstraint(self.laboratory_soft_constraint, ["laboratory"])
            self.problem.addConstraint(self.time_constraint, ["timeslot"])
            solutions = self.problem.getSolutions()

        return solutions
    

    def instructors_constraint(self, instructor):
        if (
            instructor.expertise is not None
            and instructor.expertise.name == self.course
        ):
            return True
        return False

    def laboratory_soft_constraint(self, laboratory):
        if self.laboratory is not None:
            return self.laboratory == laboratory.name
        special_courses = (
            laboratory.course.replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .split(", ")
        )
        if special_courses[0] == "":
            return True
        return False

    def laboratory_constraint(self, laboratory):
        if self.laboratory is not None:
            return self.laboratory == laboratory.name

        special_courses = (
            laboratory.course.replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .split(", ")
        )

        if self.course not in special_courses:
            return False

        return True

    def time_constraint(self, timeslot):
        schedules = Schedule.objects.filter(section=self.section).all()
        time = self.get_time(timeslot)

        for schedule in schedules:
            start = self.get_time(schedule.time_start)
            end = self.get_time(schedule.time_end)
            if (
                time >= start
                and time < end
                and timeslot.split(" ")[0] == schedule.time_start.split(" ")[0]
            ):
                return False

        return True

    def get_time(self, time):
        time_format = "%I:%M %p"
        time_arr = time.split(" ")
        time_arr.pop(0)
        time = " ".join(time_arr)
        value = datetime.strptime(time, time_format).time()

        return value
