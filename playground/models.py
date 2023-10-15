from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=4)


class Year(models.Model):
    year = models.IntegerField()


class SectionName(models.Model):
    name = models.CharField(max_length=255)


class Course(models.Model):
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    units = models.IntegerField()


class Laboratory(models.Model):
    name = models.CharField(max_length=255)
    course = models.TextField()


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    expertise = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)


class Day(models.Model):
    name = models.CharField(max_length=255)


class Section(models.Model):
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    year = models.ForeignKey(Year, null=True, on_delete=models.SET_NULL)
    section_name = models.ForeignKey(SectionName, null=True, on_delete=models.SET_NULL)


class Schedule(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    day = models.ForeignKey(Day, null=True, on_delete=models.SET_NULL)
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)
    laboratory = models.ForeignKey(Laboratory, null=True, on_delete=models.SET_NULL)
    time_start = models.TimeField()
    time_end = models.TimeField()
