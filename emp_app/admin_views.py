from django.shortcuts import render, redirect




from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from emp_app.forms import NotificationForm, UsersRegister, PanchayathRegister, LoginRegister, SchemeForm


# def tst(request):
#     return render(request,'tst.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:
                print("okk")
                return redirect('admin_dash')
            elif user.is_users:
                print("user")
                return redirect('user_dashboard')
            elif user.is_panchayath:
                print("is_panchayath")
                return redirect('panchayath_dashboard')


        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def admin_dashboard(request):
    return render(request, "admin_dashboard_base.html")


def user_dashboard(request):
    return render(request, "user_base.html")


def panchayath_dashboard(request):
    return render(request, "panchayath.html")


def test(request):
    data = NotificationForm()
    return render(request, 'test.html', {"form": data})


class RegistrationView(View):
    def get(self, request):
        user = LoginRegister()
        panchayath_form = PanchayathRegister()
        user_form = UsersRegister()
        return render(request, 'tst.html', {"user": user, "panchayath_form": panchayath_form, "user_form": user_form})

    def post(self, request):
        user = LoginRegister(request.POST)
        panchayath_form = PanchayathRegister(request.POST, request.FILES)
        user_form = UsersRegister(request.POST, request.FILES)

        if user.is_valid() and user_form.is_valid():

            a = user.save(commit=False)
            print(a)
            a.is_users = True
            a.save()
            user1 = user_form.save(commit=False)
            print(user1)
            user1.user = a
            user1.save()
            return redirect('login_view')


        elif user.is_valid() and panchayath_form.is_valid():
            print("2")
            s = user.save(commit=False)
            s.is_panchayath = True
            s.save()
            user1 = panchayath_form.save(commit=False)
            user1.user = s
            user1.save()
            return redirect('login_view')

        return render(request, 'tst.html', {"user": user, "panchayath_form": panchayath_form, "user_form": user_form})





from emp_app.models import Panchayath, users, Notification, Complaints, AddScheme, Payments


def view_panchayath(request):
    data = Panchayath.objects.all()

    return render(request,'admin/panchayath_table.html', {'data': data})

def delete_panchayath(request,id):
    data = Panchayath.objects.get(id=id)
    data.delete()
    return redirect('view_panchayath')


def view_users(request):
    data = users.objects.all()

    return render(request,'admin/users_table.html', {'data': data})

def delete_users(request,id):
    data = users.objects.get(id=id)
    data.delete()
    return redirect('view_users')


def notify(request):
    form = NotificationForm()
    if request.method == 'POST':
        obj = NotificationForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("notification")
    return render(request, 'admin/notification.html', {'form': form})

def notifications(request):
    data = Notification.objects.all()
    return render(request,'admin/notification_view.html',{'data':data})



def delete_notify(request,id):
    data = Notification.objects.get(id=id)
    data.delete()
    return redirect('notification')


def feedbacks(request):
    n = Complaints.objects.all()
    return render(request,'admin/feedbacks.html',{'feedbacks':n})

def reply_feedback(request,id):
    feedback = Complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('feedbacks')
    return render(request, 'admin/admin_feedback.html', {'feedback': feedback})


def Add_scheme(request):
    form = SchemeForm()
    if request.method == 'POST':
        obj = SchemeForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("view_scheme")
    return render(request,'admin/add_scheme.html', {'form': form})


def view_scheme(request):
    data = AddScheme.objects.all()
    return render(request,'admin/scheme.html',{'data':data})


def delete_scheme(request,id):
    data = AddScheme.objects.get(id=id)
    data.delete()
    return redirect('view_scheme')

def payment_admin(request):
    data = Payments.objects.all()
    return render(request,'admin/payment_admin.html',{'data':data})

