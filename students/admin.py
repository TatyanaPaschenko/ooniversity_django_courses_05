from django.contrib import admin
from students.models import Student
from django.db import models
from django.forms import widgets


class StudentAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "skype"]
    list_filter = ["courses"]
    search_fields = ["surname", "email"]
    filter_horizontal = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']})
    ]


admin.site.register(Student, StudentAdmin)
