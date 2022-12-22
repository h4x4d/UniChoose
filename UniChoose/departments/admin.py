from django.contrib import admin

from departments.models import Department, WeightedDepartment

admin.site.register(Department)
admin.site.register(WeightedDepartment)
