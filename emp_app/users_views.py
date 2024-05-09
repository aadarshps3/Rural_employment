from django.contrib import messages
from django.shortcuts import render, redirect

from emp_app.forms import FeedbackForm
from emp_app.models import Notification, Complaints, AppointmentSchedule, users, Appointment, CreateWork, Panchayath, \
    Payments


def view_notification(request):
    data = Notification.objects.all()
    return render(request,'users/notification_view.html', {'data': data})



def feedback(request):
    form=FeedbackForm
    u= request.user

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"thank you for your feedback...!!!")
            return redirect('feedback_view')
    else:
        form = FeedbackForm()
    return render(request,'users/add_feedback.html',{'form':form})


def feedback_view(request):

    u = Complaints.objects.filter(user=request.user)
    return render(request,"users/feedback.html",{'feedback':u})


from django.contrib.auth.decorators import login_required


@login_required
def schedule_cus(request):
    current_user = request.user
    print(current_user,"**********************")
    if hasattr(current_user, 'user'):
        user_panchayath = current_user.user.all().first().panchayath_name
        print(user_panchayath,"!@#$%^&*")
        if user_panchayath:
            s = AppointmentSchedule.objects.filter(user=user_panchayath)
        else:
            s = AppointmentSchedule.objects.none()
    else:
        s = AppointmentSchedule.objects.none()
    context = {
        'schedule': s,
    }
    return render(request, 'users/cus_schedule.html', context)


def take_appointment(request, id):
    schedule = AppointmentSchedule.objects.get(id=id)
    u = users.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u , schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Applied for this job')
        return redirect("schedule_cus")
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Your Job Application Recieved')
            return redirect('appointments')
    return render(request, 'users/take_appointment.html', {'schedule': schedule})

def appointments(request):
    u = users.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'users/cus_appointment.html', {'appointment': a})


def view_works(request):
    u = request.user
    print(u)
    data = CreateWork.objects.filter(work__user__user= u)
    # data = CreateWork.objects.all()

    return render(request,'users/work.html',{'data':data})

def cus_payment(request):
    u=users.objects.get(user=request.user)
    data = Payments.objects.filter(customer_name=u)
    return render(request,'users/cus_payment.html',{'data':data})

