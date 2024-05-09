from emp_app import views, admin_views, users_views, panchayath_views
from django.urls import path

from emp_app.views import RegistrationView

urlpatterns = [
    # path("",views.tst,name="tst"),
    path('', RegistrationView.as_view(), name='registration'),
    # path('', views.Panchayath_registration, name='registration'),
    # path('reg_user', views.User_registration, name='reg_user'),
    path("login_view",views.login_view,name="login_view"),
    path("admin_dash",views.admin_dashboard,name="admin_dash"),
    path("user_dashboard",views.user_dashboard,name="user_dashboard"),
    path("panchayath_dashboard",views.panchayath_dashboard,name="panchayath_dashboard"),
    path("test",views.test,name="test"),
    path("logout_view/", views.logout_view, name='logout_view'),

    #ADMIN
    path('view_panchayath',admin_views.view_panchayath,name="view_panchayath"),
    path('delete_panchayath/<int:id>/',admin_views.delete_panchayath,name="delete_panchayath"),
    path('view_users',admin_views.view_users,name="view_users"),
    path('delete_users/<int:id>/',admin_views.delete_users,name="delete_users"),
    path('feedbacks', admin_views.feedbacks, name='feedbacks'),
    path('reply_feedback/<int:id>/',admin_views.reply_feedback,name = 'reply_feedback'),


    path('notify',admin_views.notify,name="notify"),
    path('notification',admin_views.notifications,name='notification'),
    path('delete_notify/<int:id>/',admin_views.delete_notify,name='delete_notify'),

    path("Add_scheme",admin_views.Add_scheme,name='Add_scheme'),
    path("view_scheme",admin_views.view_scheme,name='view_scheme'),
    path("delete_scheme/<int:id>/",admin_views.delete_scheme,name='delete_scheme'),
    path("payment_admin",admin_views.payment_admin,name='payment_admin'),


    #users
    path('view_notification',users_views.view_notification,name='view_notification'),
    path("feedback",users_views.feedback,name="feedback"),
    path("feedback_view", users_views.feedback_view, name="feedback_view"),
    path('schedule_cus',users_views.schedule_cus,name='schedule_cus'),
    path('take_appointment/<int:id>/',users_views.take_appointment, name='take_appointment'),
    path('appointments', users_views.appointments, name='appointments'),
    path("works",users_views.view_works,name='view_works'),
    path("cus_payment",users_views.cus_payment,name='cus_payment'),

    #panchayath

    path('notifications',panchayath_views.notification,name='notifications'),
    path('view_schemes',panchayath_views.view_scheme,name='view_schemes'),
    path('schedule',panchayath_views.schedule_add,name='schedule'),
    path('schedule_view',panchayath_views.schedule,name='schedule_view'),
    path('sch_delete/<int:id>/', panchayath_views.schedule_delete, name='sch_delete'),
    path('Payment', panchayath_views.Payment, name='Payment'),
    path('Payment_view', panchayath_views.Payment_view, name='Payment_view'),

    path('appointment_panchayath', panchayath_views.appointment_panchayath, name='appointment_panchayath'),
    path('approve_appointment/<int:id>/', panchayath_views.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', panchayath_views.reject_appointment, name='reject_appointment'),
    path('Creatework/<int:id>/',panchayath_views.Creatework,name='Creatework'),
    path("work",panchayath_views.view_work,name='view_work'),
    path('update/<int:id>/',panchayath_views.update,name='update'),
]
