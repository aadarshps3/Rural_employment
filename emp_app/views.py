from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from emp_app.forms import NotificationForm, UsersRegister, PanchayathRegister, LoginRegister


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
            login(request,user)
            if user.is_staff:

                return redirect('admin_dash')
            elif user.is_users:

                return redirect('user_dashboard')
            elif user.is_panchayath:

                return redirect ('panchayath_dashboard')


        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'login.html')


def admin_dashboard(request):
    return render(request,"admin_dashboard_base.html")

def user_dashboard(request):
    return render(request,"user_base.html")

def panchayath_dashboard(request):
    return render(request,"panchayath.html")


def test(request):
    data = NotificationForm()
    return render(request,'test.html',{"form":data})



class RegistrationView(View):
    def get(self, request):
        user = LoginRegister()
        panchayath_form = PanchayathRegister()
        user_form = UsersRegister()
        return render(request, 'tst.html', {"user": user, "panchayath_form": panchayath_form, "user_form": user_form})

    def post(self, request):
        user = LoginRegister(request.POST)
        panchayath_form = PanchayathRegister(request.POST, request.FILES)
        user_form = UsersRegister(request.POST,request.FILES)

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





def logout_view(request):
    logout(request)
    return redirect('login_view')