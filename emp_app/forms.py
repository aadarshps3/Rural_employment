from django import forms
from django.contrib.auth.forms import UserCreationForm

from emp_app.models import Notification, users, Panchayath, Login_view, Complaints, AddScheme, AppointmentSchedule, \
    CreateWork, Payments


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login_view
        fields = ('username','password1','password2',)


class UsersRegister(forms.ModelForm):

    class Meta:
        model = users
        fields = "__all__"
        exclude = ("user",)

class PanchayathRegister(forms.ModelForm):

    class Meta:
        model = Panchayath
        fields = "__all__"
        exclude = ("user",)




class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('__all__')



class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Complaints
        fields = ('feedback',)


class SchemeForm(forms.ModelForm):

    class Meta:
        model = AddScheme
        fields = ('__all__')


class DateInput(forms.DateInput):
    input_type = 'date'



class ScheduleAdd(forms.ModelForm):

    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)

    class Meta:
        model = AppointmentSchedule
        fields = ('scheme', 'start_date','end_date','designation','qualifications')
        exclude = ('user',)


class WorkForm(forms.ModelForm):

    class Meta:
        model = CreateWork
        fields = ('__all__')
        exclude = ('work',)

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'