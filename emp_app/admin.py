from django.contrib import admin

# Register your models here.
from emp_app import models
from emp_app.models import Notification, Panchayath, users, Login_view, CreateWork, Appointment

admin.site.register(Notification)
admin.site.register(Panchayath)
admin.site.register(users)





admin.site.register(Login_view)
admin.site.register(CreateWork)
admin.site.register(Appointment)