from django.contrib import messages
from django.shortcuts import render, redirect

from emp_app.forms import ScheduleAdd, WorkForm, PaymentsForm
from emp_app.models import Notification, AddScheme, AppointmentSchedule, Panchayath, Appointment, CreateWork, Payments


def notification(request):
    data = Notification.objects.all()
    return render(request,'panchayath/notifications.html',{'data':data})



def view_scheme(request):
    data = AddScheme.objects.all()
    return render(request,'panchayath/schemes.html', {'data': data})


def schedule_add(request):
    s = request.user
    u = Panchayath.objects.get(user=s)
    print(u)
    form = ScheduleAdd()
    if request.method == 'POST':
        form = ScheduleAdd(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Job Added Successfully')
            return redirect('schedule_view')
    else:
        form = ScheduleAdd()
    return render(request, 'panchayath/schedule_add.html', {'form': form})


def schedule(request):
    u=Panchayath.objects.get(user=request.user)
    n = AppointmentSchedule.objects.filter(user=u)

    context = {
        'schedule': n,
    }
    return render(request, 'panchayath/schedule_view.html', context)


def schedule_delete(request, id):
    data = AppointmentSchedule.objects.get(id=id)
    data.delete()
    messages.info(request, 'Deleted Successfully')
    return redirect('schedule_view')




def appointment_panchayath(request):
    u = request.user
    panchayath = Panchayath.objects.get(user = u)
    print(panchayath)
    p = Appointment.objects.filter(schedule__user=panchayath)


    context = {
        'appointment': p,
     }
    return render(request, 'panchayath/appointment.html', context)




def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Approved')
    return redirect('appointment_panchayath')


def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request,'Rejected')
    return redirect('appointment_panchayath')


def Creatework(request,id):

        data= Appointment.objects.get(id=id)
        print(data)
        form = WorkForm()

        if request.method == 'POST':
            form = WorkForm(request.POST)
            if form.is_valid():
                data.status2 = 2
                data.save()

                obj = form.save(commit=False)
                obj.work = data
                obj.save()
                data.status = 3
                data.save()

                messages.info(request, 'Work created')
                return redirect('appointment_panchayath')
        return render(request, 'panchayath/work_add.html', {'form': form})


def view_work(request):
    u = request.user
    data = CreateWork.objects.filter(work__schedule__user__user = u)

    return render(request,'panchayath/work.html',{'data':data})


def update(request,id):
    n = CreateWork.objects.get(id=id)
    if request.method == 'POST':
        form = WorkForm(request.POST, instance=n)
        if form.is_valid():
            form.save()
            return redirect('view_work')
    else:
        form = WorkForm(instance=n)
    return render(request, 'panchayath/update.html', {'form': form})

def Payment(request):
    form = PaymentsForm()
    if request.method == 'POST':
        form = PaymentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Payment Added")
            return redirect('Payment_view')
    return render(request,'panchayath/Payment_add.html',{'form':form})

def Payment_view(request):
    data = Payments.objects.all()
    return render(request,'panchayath/Payment_views.html',{'data':data})