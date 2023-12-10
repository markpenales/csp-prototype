from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=4)
    
    def __str__(self):
        return self.code


class Year(models.Model):
    year = models.IntegerField()
    
    def __str__(self):
        return str(self.year)


class SectionName(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    units = models.IntegerField()
    
    def __str__(self):
        return self.name


class Laboratory(models.Model):
    name = models.CharField(max_length=255)
    course = models.TextField()
    
    def get_schedules(self):
        return Schedule.objects.filter(laboratory=self)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.course}"


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    expertise = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def get_schedules(self):
        schedules = Schedule.objects.filter(instructor=self)
        return schedules.all()

class Day(models.Model):
    name = models.CharField(max_length=255)


class Section(models.Model):
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    section_name = models.ForeignKey(SectionName, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.program.code} {self.year.year}{self.section_name.name}"


class Schedule(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    day = models.ForeignKey(Day, null=True, on_delete=models.SET_NULL)
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)
    laboratory = models.ForeignKey(Laboratory, null=True, on_delete=models.SET_NULL)
    time_start = models.CharField(max_length=255)
    time_end = models.CharField(max_length=255)
    
