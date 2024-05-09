from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login_view(AbstractUser):
    is_users = models.BooleanField(default=False)
    is_panchayath = models.BooleanField(default=False)

class Panchayath(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name="panchayath")
    panchayath_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.panchayath_name

class users(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE,related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    panchayath_name = models.ForeignKey(Panchayath,on_delete=models.CASCADE,null=True,blank=True)
    adhar_number = models.CharField(max_length=16)
    Resume = models.FileField(upload_to='Resume/')

    def __str__(self):
        return self.name









class Notification(models.Model):
    message= models.CharField(max_length=100)
    date = models.DateField(auto_now=True)


class AddScheme(models.Model):
    scheme_name =  models.CharField(max_length=100)
    scheme_fund = models.CharField(max_length=100)
    scheme_tenure = models.CharField(max_length=100)

    def __str__(self):
        return self.scheme_name


class Complaints(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)



class AppointmentSchedule(models.Model):
    QUALIFICATION_CHOICES = (
        ('high_school', 'High School'),
        ('Degree', 'Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
    )
    user = models.ForeignKey(Panchayath, on_delete=models.DO_NOTHING)
    scheme = models.ForeignKey(AddScheme, on_delete=models.DO_NOTHING)
    qualifications = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    designation = models.CharField(max_length=50)



class Appointment(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(AppointmentSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    status2 = models.IntegerField(default=0)


class CreateWork(models.Model):
    work = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING, related_name='work')
    stat = (('started', 'started'), ('50% done', '50% done'), ('completed', 'completed'))
    status = models.CharField(max_length=50, choices=stat, default='Pending', null=True)
    work_file_number = models.CharField(max_length=5)
    description = models.CharField(max_length=500, null=False)

    Total_fund = models.CharField(max_length=10,default=0,null=True)
    paystat = (('Advance paid ','Advance paid'),('Payment completed', 'Payment completed'))
    statuspay = models.CharField(max_length=50, choices=paystat, default='Not paid', null=True)

class Payments(models.Model):
    customer_name = models.ForeignKey(users,on_delete=models.CASCADE)
    Amount = models.CharField(max_length=10,null=True,blank=True)
    card_number = models.CharField(max_length=16)
    expiry = models.CharField(max_length=10)
    cvv = models.CharField(max_length=3)
    date = models.DateField(auto_now=True)



