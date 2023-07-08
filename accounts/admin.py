from django.contrib import admin
from .models import (
    Classroom,
    Student,
    Subject,
    Teacher,
    Leave,
    Attendance
)

# Register your models here.
# admin.site.register(Classroom)
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display=['id','name']
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','current_class']
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['id','name']
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name']
@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display=['id','email']
admin.site.register(Attendance)








# class base view
# remove json parse