from django.contrib import admin

# Register your models here.
from firstapp.models import employee
class employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','eaddr']

admin.site.register(employee,employeeadmin)
