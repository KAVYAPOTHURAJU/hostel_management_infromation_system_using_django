from   authenticate import views
from django.urls import path



urlpatterns = [
    path('home/', views.home, name ="home"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('logoutadmin/', views.logoutadmin, name='logoutadmin'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('fee/', views.fee, name ="fee"),
    path('mess/', views.mess, name ="mess"),
    path('rooms/', views.rooms, name ="rooms"),
    path('bookings/', views.bookings, name ="bookings"),
    path('', views.index, name ="index"),
    path('Sayhi/', views.Sayhi, name ="Sayhi"),
    path('services/', views.services, name ="services"),
    path('seeinfo/', views.seeinfo, name ="seeinfo"),
    path('availableroom/',views.availableroom,name ='availableroom'),
    path('bookingdetails/',views.bookingdetails,name ='bookingdetails'),
    path('commentsresponse/',views.commentsresponsefromadmin,name='commentsresponse'),
    path('outingform/',views.outingform,name="outingform"),
    path('outingresponse/',views.outingresponsefromadmin,name="outingresponse"),
    path('visitorsform/',views.vistorsform,name="visitorsform"),
    path('adminindex/',views.adminindex,name="adminindex"),
    path('adminreg/',views.adminreg,name="adminreg"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminloginhome/',views.adminloginhome,name="adminloginhome"),
    path('adminrooms/',views.adminrooms,name="adminrooms"),
    path('adminpaymentview/',views.adminpaymentview,name="adminpaymentview"),
    path('studentinfo/',views.studentinfo,name="studentinfo"),
    path('addingstudents/',views.addingstudents,name="addingstudents"),
    path('adminoutingandcomments/',views.adminoutingandcomments,name="adminoutingandcomments"),
    path('searchdata/',views.searchdata,name="searchdata"),
    path('studentinformation/',views.studentinformation,name="studentinformation"),
    path('roompayment/',views.roompayment,name="roompayment"),
    path('paymentmess/',views.paymentmess,name="paymentmess"),
    path('servicesform/',views.servicesform,name="servicesform"),
    path('serviceresponse/',views.serviceresponse,name="serviceresponse"),
    path('notice/',views.notice,name="notice"),
    path('wardenreq/',views.wardenreq,name="wardenreq"),
    path('addingrooms/',views.addingrooms,name="addingrooms"),
    path('adminservices/',views.dispservice,name="adminservices"),
    path('editservice/<int:id>/',views.editservice,name="editservice"),
    path('Update/<int:id>/',views.updateservices,name="updateservices"),
    path('complaintform/',views.complaintform,name="complaintform"),
    path('complaintsresponse/',views.complaintsresponse,name="complaintsresponse")
    
]

