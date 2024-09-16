from django.contrib import admin
from .models import Faculty, Department, Teacher, Student, Group, University

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faculty')
    search_fields = ('name',)
    list_filter = ('faculty',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    search_fields = ('name',)
    list_filter = ('department',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group')
    search_fields = ('name',)
    list_filter = ('group',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    search_fields = ('name',)
    list_filter = ('department',)

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    filter_horizontal = ('faculties',)