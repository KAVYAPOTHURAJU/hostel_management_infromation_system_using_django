from django.contrib.auth.backends import UserModel
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, UsernameField 
from django.contrib import messages
from authenticate.models import  BookingForm,DetailsofStudent,Availability_room,Commentsinfo,OutingFormforstudents,Visitor,Adminuser,RoomPaymentForm,MessPaymentForm,ServicesOfHostel,Notice,Msg_from_warden,Complaint
from authenticate.forms import SignUpForm, EditProfileForm,serviceforms
from django.http import HttpResponse
import datetime 

# Create your views here.
def home(request): 
	return render(request, 'authenticate/home.html', {})
def adminloginhome(request): 
	return render(request, 'authenticate/adminloginhome.html', {})
def  confirmpayment(request): 
	return render(request, 'authenticate/confirmpayment.html', {}) 
def index(request): 
	return render(request, 'authenticate/index.html', {})
def adminrooms(request): 
	return render(request, 'authenticate/adminrooms.html', {})
def Sayhi(request): 
	return render(request, 'authenticate/Sayhi.html', {})
def services(request): 
	return render(request, 'authenticate/services.html', {})
def mess(request):
	return render(request, 'authenticate/mess.html', {})
def seeinfo(request): 
	return render(request, 'authenticate/seeinfo.html', {})
def adminindex(request): 
	return render(request, 'authenticate/adminindex.html', {})
def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('You are logged in'))
			return redirect('home') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('index')

def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('home')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('home')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})



def adminreg(request):
	if request.method =='POST':
		Username=request.POST['User']
		Email=request.POST['email']
		Password=request.POST['pwd']
		Adminuser(Username=Username,Email=Email,Password=Password).save()
		messages.success(request, ('Your account is succesfully created'))
		return render(request,'authenticate/adminreg.html')
	else:
		return render(request,'authenticate/adminreg.html')
def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('index')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)
def fee(request):
	return render(request, 'authenticate/fee.html', {})
def rooms(request):
	return render(request, 'authenticate/rooms.html', {})
def bookings(request):
	if request.method=='POST':
	  Username=request.POST['UserName']
	  Email=request.POST['email']
	  Education=request.POST['edu']
	  Gender= request.POST['gender']
	  Room_no =request.POST['roomno']
	  room_type = request.POST['roomtype']
	  checkIn=request.POST['checkin']
	  checkOut=request.POST['checkout']
	  price = request.POST['priceofroom']
	  BookingForm(Username=Username,Email=Email,Education=Education,Gender=Gender,Room_no=Room_no,room_type =room_type ,checkIn=checkIn,checkOut=checkOut,price=price).save()
	  messages.success(request, ('You have booked a room'))
	  return render(request,'authenticate/bookings.html')
	else:
		return render(request,'authenticate/bookings.html')

	
def availableroom(request):
    data = Availability_room .objects.all()
    info = {
           "data": data
           }
    return render(request,'authenticate/availableroom.html', info)
def studentinformation(request):
    infoofstudent = DetailsofStudent .objects.all()
    hostelstu = {
           "infoofstudent":infoofstudent
           }
    return render(request,'authenticate/studentinformation.html', hostelstu)
def adminrooms(request):
    datas = Availability_room .objects.all()
    return render(request,'authenticate/adminrooms.html', {"Availability_room":datas})
def bookingdetails(request):
    bookingdata = BookingForm .objects.all()
    booking = {
           "bookingdata":bookingdata
           }
    return render(request,'authenticate/bookingdetails.html',booking)
'''def commentsresponse(request):
    userinfo = Commentsinfo .objects.all()
    comments = {
           "userinfo":userinfo
           }
    return render(request,'authenticate/commentsresponse.html',comments)'''

def Sayhi(request):
	if request.method=='POST':
	  Username=request.POST['UserName']
	  Email=request.POST['email']
	  Postcomment=request.POST['comments']
	  Askadmin=request.POST['admin']
	  Commentsinfo(Username=Username,Email=Email,Postcomment=Postcomment,Askadmin=Askadmin ).save()
	  messages.success(request, ('You have posted your query !! We will get back to you soon!!'))
	  return render(request,'authenticate/Sayhi.html')
	else:
		return render(request,'authenticate/Sayhi.html')
def vistorsform(request):
	if request.method=='POST':
	  Username=request.POST['UserName']
	  Email=request.POST['email']
	  Room_no=request.POST['roomno']
	  Block_no =request.POST['block']
	  StudentPhonenumber=request.POST['snumber']
	  Firstvisitor=request.POST['vfname']
	  VistorPhonenumber=request.POST['vfnumber']
	  Secondvisitor=request.POST['vsname']
	  SecondVistorPhonenumber=request.POST['vsnumber']
	  Visitor(Username=Username,Email=Email,Room_no=Room_no,Block_no=Block_no,StudentPhonenumber=StudentPhonenumber,Firstvisitor=Firstvisitor, VistorPhonenumber= VistorPhonenumber,Secondvisitor=Secondvisitor,SecondVistorPhonenumber=SecondVistorPhonenumber).save()
	  messages.success(request, ('You have posted your visitors details!'))
	  return render(request,'authenticate/visitorsform.html')
	else:
		return render(request,'authenticate/visitorsform.html') 
	
def outingform(request):
	if request.method=='POST':
		Username=request.POST['UserName']
		Email=request.POST['email']
		Room_no =request.POST['roomno']
		Block_no =request.POST['block']
		checkOut=request.POST['checkout']
		checkIn=request.POST['checkin']
		Purpose=request.POST['purpose']
		StudentPhonenumber=request.POST['snumber']
		Parentname=request.POST['pname']
		ParentPhonenumber=request.POST['pnumber']
		Approval=request.POST['approval']
		OutingFormforstudents(Username=Username,Email=Email,Room_no=Room_no,Block_no=Block_no,checkOut=checkOut,checkIn=checkIn,Purpose=Purpose,StudentPhonenumber=StudentPhonenumber,Parentname=Parentname,ParentPhonenumber=ParentPhonenumber,Approval=Approval).save()
		messages.success(request, ('You have successfully submitted your outingform request...We will get back to you soon'))
		return render(request,'authenticate/outingform.html')
	else:
		return render(request,'authenticate/outingform.html')


def outingresponses(request):
    outing = OutingFormforstudents .objects.all()
    datainfo = {
           "outing":outing
           }
    return render(request,'authenticate/outingresponse.html',datainfo)
def adminlogin(request):
	if request.method=='POST':
		try:
			user=Adminuser.objects.get(Username=request.POST['User'],Password=request.POST['pwd'])
			print("Username=",user)
			request.session['User']=user.Username
			messages.success(request, ('You are logged in'))
			return render(request,'authenticate/adminloginhome.html')
		except Adminuser.DoesNotExist as e:
			messages.success(request, ('User does not exist'))
	return render(request,'authenticate/adminlogin.html')
def adminpaymentview(request):
	roomdata =RoomPaymentForm  .objects.all()
	messdata= MessPaymentForm .objects .all()
	return render(request,'authenticate/adminpaymentview.html',{"RoomPaymentForm":roomdata,  "MessPaymentForm":messdata})
def addingrooms(request):
	if request.method=='POST':
		Room_no =request.POST['roomno']
		Block_no =request.POST['block']
		available_persons =request.POST['ap']
		room_type=request.POST['roomtype']
		vacancy=request.POST['vac']
		price=request.POST['price']
		Availability_room(Room_no=Room_no,Block_no=Block_no,available_persons=available_persons,room_type=room_type,vacancy=vacancy,price=price).save()
		messages.success(request, ('You have added a room detail'))
		return render(request,'authenticate/addingrooms.html')
	else:
		return render(request,'authenticate/addingrooms.html')

def addingstudents(request):
	if request.method=='POST':
	  Username=request.POST['User']
	  Email=request.POST['email']
	  Education=request.POST['edu']
	  Gender= request.POST['gender']
	  Room_no =request.POST['roomno']
	  room_type = request.POST['roomtype']
	  price = request.POST['price']
	  checkIn=request.POST['checkin']
	  checkOut=request.POST['checkout']
	  Room_Payment_status=request.POST['rp']
	  Mess_Payment_status=request.POST['mp']
	  StudentPhonenumber=request.POST['sp']
	  DetailsofStudent(Username=Username,Email=Email,Education=Education,Gender=Gender,Room_no=Room_no,room_type =room_type ,price=price,checkIn=checkIn,checkOut=checkOut,Room_Payment_status=Room_Payment_status,Mess_Payment_status=Mess_Payment_status,StudentPhonenumber=StudentPhonenumber).save()
	  messages.success(request, ('You have added a student detail'))
	  return render(request,'authenticate/addingstudents.html')
	else:
		return render(request,'authenticate/addingstudents.html')
def studentinfo(request):
	studentdata =DetailsofStudent  .objects.all()
	vistordata =Visitor.objects.all()
	return render(request,'authenticate/studentinfo.html',{"DetailsofStudent":studentdata,"Visitor":vistordata})
		
def adminoutingandcomments(request):
	odata =Commentsinfo .objects.all()
	cdata =OutingFormforstudents.objects.all()
	sdata=ServicesOfHostel.objects.all()
	compdata=Complaint.objects.all()
	return render(request,'authenticate/adminoutingandcomments.html',{"Commentsinfo":odata,"OutingFormforstudents":cdata,"ServicesOfHostel":sdata,"Complaint":compdata})
def searchdata(request):
	if request.method=='POST':
		Username=request.POST.get('Username')
		sobj=DetailsofStudent.objects.raw('SELECT * FROM authenticate_detailsofstudent where  Username="'+Username+'"')
		return render(request,'authenticate/searchdata.html',{"infoofstudent":sobj})
	else:
		s1obj=DetailsofStudent.objects.raw('SELECT * FROM authenticate_detailsofstudent')
		return render(request,'authenticate/searchdata.html')
def notice(request):
	if request.method=='POST':
		Username=request.POST.get('Username')
		nobj=Notice.objects.raw('SELECT * FROM authenticate_notice where  Username="'+Username+'"')
		return render(request,'authenticate/notice.html',{"noticeinfo":nobj})
	else:
		n1obj=Notice.objects.raw('SELECT * FROM authenticate_notice')
		return render(request,'authenticate/notice.html')
def outingresponsefromadmin(request):
	if request.method=='POST':
		Username=request.POST.get('Username')
		outingobj=Commentsinfo.objects.raw('SELECT * FROM authenticate_outingformforstudents where  Username="'+Username+'"')
		return render(request,'authenticate/outingresponse.html',{"outing":outingobj})
	else:
		outing1obj=Commentsinfo.objects.raw('SELECT * FROM authenticate_outingformforstudents')
		return render(request,'authenticate/outingresponse.html')
def commentsresponsefromadmin(request):
	if request.method=='POST':
		Username=request.POST.get('Username')
		commentobj=OutingFormforstudents.objects.raw('SELECT * FROM authenticate_commentsinfo where  Username="'+Username+'"')
		return render(request,'authenticate/commentsresponse.html',{"userinfo":commentobj})
	else:
		comment1obj=OutingFormforstudents.objects.raw('SELECT * FROM authenticate_commentsinfo')
		return render(request,'authenticate/commentsresponse.html')
def roompayment(request):
	if request.method=='POST':
	  Username=request.POST['UserName']
	  Email=request.POST['email']
	  Education=request.POST['edu']
	  Gender= request.POST['gender']
	  Room_no =request.POST['roomno']
	  Block_no =request.POST['block']
	  room_type = request.POST['roomtype']
	  price = request.POST['priceofroom']
	  Transactionid=request.POST['id']
	  Receipt=request.FILES['myfile']
	  RoomPaymentForm(Username=Username,Email=Email,Education=Education,Gender=Gender,Room_no=Room_no,Block_no=Block_no,room_type =room_type,price=price,Transactionid=Transactionid,Receipt=Receipt).save()
	  messages.success(request, ('You have successfully submitted your payment details'))
	  return render(request,'authenticate/roompayment.html')
	else:
		return render(request,'authenticate/roompayment.html')
def paymentmess(request):
	if request.method=='POST' :
	  Username=request.POST['UserName']
	  Email=request.POST['email']
	  Education=request.POST['edu']
	  Gender= request.POST['gender']
	  Room_no =request.POST['roomno']
	  food_category=request.POST['food']
	  Block_no =request.POST['block']
	  price = request.POST['priceofmess']
	  Transactionid=request.POST['id']
	  Receipt=request.FILES['myfile']
	  MessPaymentForm(Username=Username,Email=Email,Education=Education,Gender=Gender,Room_no=Room_no,food_category=food_category,Block_no=Block_no,price=price,Transactionid=Transactionid,Receipt=Receipt).save()
	  messages.success(request, ('You have successfully submitted your payment details'))
	  return render(request,'authenticate/paymentmess.html')
	else:
		return render(request,'authenticate/paymentmess.html')
def servicesform(request):
	if request.method=='POST' :
	  Username=request.POST['UserName']
	  Room_no =request.POST['roomno']
	  Block_no =request.POST['block']
	  Service_required=request.POST['ser']
	  Askadmin=request.POST['admin']
	  ServicesOfHostel(Username=Username,Room_no=Room_no,Block_no=Block_no,Service_required=Service_required,Askadmin=Askadmin).save()
	  messages.success(request, ('You have successfully submitted your service form'))
	  return render(request,'authenticate/servicesform.html')
	else:
		return render(request,'authenticate/servicesform.html')
def serviceresponse(request):
	if request.method=='POST':
		Username=request.POST.get('Username')
		ser1obj=ServicesOfHostel.objects.raw('SELECT * FROM authenticate_hostelservices where  Username="'+Username+'"')
		return render(request,'authenticate/serviceresponse.html',{"serviceinfo":ser1obj})
	else:
		serobj1=ServicesOfHostel.objects.raw('SELECT * FROM authenticate_hostelservices')
		return render(request,'authenticate/serviceresponse.html')


def dispservice(request):
	results =ServicesOfHostel.objects.all()
	return render(request,'authenticate/adminservices.html',{"ServicesOfHostel":results})
def editservice(request,id):
	editservice=ServicesOfHostel.objects.get(id=id)	
	return render(request,'authenticate/editservice.html',{"ServicesOfHostel":editservice})
 

def  updateservices(request,id):
	editservice=ServicesOfHostel.objects.get(id=id)
	form=serviceforms(request.POST,instance=editservice)
	if form.is_valid():
		form.save()
		messages.success(request, ('You have successfully added response'))
		return redirect("adminservices")
	return render(request,"authenticate/editservice.html",{"editservice":editservice})
	
	
	


def wardenreq(request):
	if request.method=='POST' :
	  Username=request.POST['UserName']
	  Room_no =request.POST['roomno']
	  Block_no =request.POST['block']
	  Wardenmsg =request.POST['msg']
	  Msg_from_warden(Username=Username,Room_no=Room_no,Block_no =Block_no ,Wardenmsg=Wardenmsg).save()
	  messages.success(request, ('You have successfully submitted your message details'))
	  return render(request,'authenticate/wardenreq.html')
	else:
		return render(request,'authenticate/wardenreq.html')

def logoutadmin(request):
	logoutadmin(request)
	messages.success(request,('Youre now logged out'))
	return redirect('index')
def complaintform(request):
	if request.method=='POST':
		Username=request.POST['UserName']
		Email=request.POST['email']
		Room_no =request.POST['roomno']
		Block_no =request.POST['block']
		Post_complaint=request.POST['complaint']
		StudentPhonenumber=request.POST['snumber']
		Askadmin=request.POST['admin']
		Complaint(Username=Username,Email=Email,Room_no=Room_no,Block_no=Block_no,Post_complaint=Post_complaint,StudentPhonenumber=StudentPhonenumber,Askadmin=Askadmin).save()
		messages.success(request, ('You have successfully registered your complaint..We will get back to you soon!!..'))
		return render(request,'authenticate/complaintform.html')
	else:
		return render(request,'authenticate/complaintform.html')
	
def complaintsresponse(request):
	if request.method=='POST':
		Username=request.POST.get('Username')
		complaintobj=Complaint.objects.raw('SELECT * FROM authenticate_complaint where  Username="'+Username+'"')
		return render(request,'authenticate/complaintsresponse.html',{"complaintinfo":complaintobj})
	else:
		complaint1obj=Commentsinfo.objects.raw('SELECT * FROM authenticate_complaint')
		return render(request,'authenticate/complaintsresponse.html')