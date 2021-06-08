from django.contrib import admin

# Register your models here.
from home.models import Student
from home.models import Contact

admin.site.register(Student)
admin.site.register(Contact)