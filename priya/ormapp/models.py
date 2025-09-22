from django.db import models
from django.contrib import admin

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    desig = models.CharField(max_length=50)
    salary = models.IntegerField()
    doj = models.DateField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id','name','desig','salary','doj')

