from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'gender', 'major', 'class_name', 'enrollment_date')
    list_filter = ('gender', 'major', 'enrollment_date')
    search_fields = ('student_id', 'name', 'major')
    ordering = ('student_id',)