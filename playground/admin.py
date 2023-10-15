from django.contrib import admin
from . import models

# Register your models here.
class SchedulingSystem(admin.AdminSite):
    site_header = "Scheduling System"
    index_title = "CSP - Scheduling System"

scheduling_site = SchedulingSystem(name="Scheduling System - Admin")

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','get_program', 'get_year')
    search_fields = ('name',)
    
    def get_program(self, obj):
        return obj.program.code
    
    def get_year(self, obj):
        return obj.year.year
    
    
    
    
    get_year.short_description = "Year Level"
    get_program.short_description = "Program"
    
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')
    search_fields = ('code', 'name')
    
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_course')
    search_fields = ('name', 'get_course')
    
    def get_course(self, obj):
        return obj.expertise.name if obj.expertise else None
    
    get_course.short_description ='Course Taught'
    
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_course',
        'get_section',
        'get_laboratory',
        'time_start',
        'time_end'
    )
    # search_fields = ('name',)
    
    def get_course(self, obj):
        return obj.course.name

    def get_section(self, obj):
        return obj.section

    def get_laboratory(self, obj):
        return obj.laboratory.name
    get_course.short_description ='Course Taught'
    get_laboratory.short_description ='Laboratory'
    get_section.short_description = 'Section'
    
class SectionNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_section')
    
    def get_section(self, obj):
        return f"{obj.program.code} {obj.year.year}{obj.section_name.name}"

scheduling_site.register(models.Program, ProgramAdmin)
scheduling_site.register(models.SectionName, SectionNameAdmin)
scheduling_site.register(models.Course, CourseAdmin)
scheduling_site.register(models.Laboratory, LaboratoryAdmin)
scheduling_site.register(models.Instructor, InstructorAdmin)
scheduling_site.register(models.Section, SectionAdmin)
scheduling_site.register(models.Schedule, ScheduleAdmin)