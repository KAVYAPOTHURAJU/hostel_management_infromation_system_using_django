from django.db import models

class BookingForm(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Education=models.CharField(max_length=150)
    Gender=models.CharField(max_length=1)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    room_type = models.CharField(max_length=150)
    checkIn=models.DateField()
    checkOut=models.DateField()
    price = models.IntegerField(default=1500)
    def __str__(self):
        return self.Username

class Availability_room(models.Model):
    Block_no=models.CharField(max_length=150)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    available_persons= models.CharField(max_length=150)
    room_type = models.CharField(max_length=150)
    vacancy= models.IntegerField()
    price = models.IntegerField(default=1500)
    def __str__(self):
       return ("Room number:"+str(self.Room_no)+",Block"+(self.Block_no)+",room type:"+(self.room_type)+" ,vacancy +"+str(self.vacancy))
class Adminuser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Password=models.CharField(max_length=150)
    def __str__(self):
       return self.Username
class Adminlogin(models.Model):
    Username=models.CharField(max_length=150)
    Password=models.CharField(max_length=150)




class DetailsofStudent(models.Model):
    Username = models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Education=models.CharField(max_length=150)
    Gender = models.CharField(max_length=150)
    Block_no=models.CharField(max_length=150)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    room_type = models.CharField(max_length=150)
    price = models.IntegerField(default=1500)
    checkIn = models.DateField()
    checkOut = models.DateField()
    Room_Payment_status=models.CharField(max_length=150)
    Mess_Payment_status=models.CharField(max_length=150)
    StudentPhonenumber=models.BigIntegerField()
    def __str__(self):
       return self.Username
    class Meta:
        db_table ="authenticate_detailsofstudent"
class Commentsinfo(models.Model):
     Username = models.CharField(max_length=150)
     Email=models.CharField(max_length=150)
     Postcomment=models.CharField(max_length=150)
     Askadmin=models.TextField(max_length=150)
     def __str__(self):
       return self.Username
class Visitor(models.Model):
     Username = models.CharField(max_length=150)
     Email=models.CharField(max_length=150)
     Room_no = models.IntegerField ()
     Block_no=models.CharField(max_length=150)
     StudentPhonenumber=models.BigIntegerField()
     Firstvisitor= models.CharField(max_length=150)
     VistorPhonenumber=models.BigIntegerField()
     Secondvisitor=models.CharField(max_length=150)
     SecondVistorPhonenumber=models.BigIntegerField()
     def __str__(self):
       return (self.Username +self.Firstvisitor)

class OutingFormforstudents(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    Block_no=models.CharField(max_length=150)
    checkOut=models.DateField()
    checkIn=models.DateField()
    Purpose=models.CharField(max_length=150)
    StudentPhonenumber= models.BigIntegerField ()
    Parentname=models.CharField(max_length=150)
    ParentPhonenumber= models.BigIntegerField()
    Approval=models.CharField(max_length=150)
    class Meta:
        db_table="authenticate_outingformforstudents"
    def __str__(self):
          return ("Room number:"+str(self.Room_no)+" ,name :"+(self.Username)+" ,Approval :"+str(self.Approval))
class RoomPaymentForm(models.Model):
              Username=models.CharField(max_length=150)
              Email=models.CharField(max_length=150)
              Education=models.CharField(max_length=150)
              Gender=models.CharField(max_length=1)
              Room_no  = models.AutoField(primary_key=True)
              Room_no = models.IntegerField ()
              Block_no=models.CharField(max_length=150)
              room_type = models.CharField(max_length=150)
              price = models.IntegerField(default=1500)
              Transactionid = models.BigIntegerField()
              Receipt = models.FileField(upload_to='static/media/')
              def __str__(self):
                       return self.Username
class MessPaymentForm(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Education=models.CharField(max_length=150)
    Gender=models.CharField(max_length=1)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    food_category=models.CharField(max_length=150)
    Block_no=models.CharField(max_length=150)
    price = models.IntegerField(default=1500)
    Transactionid = models.BigIntegerField()
    Receipt = models.FileField(upload_to='static/media/')
    def __str__(self):
          return (self.Username+" ,Room number:"+str(self.Room_no)+",Block"+(self.Block_no)+"price ="+str(self.price))
class ServicesOfHostel(models.Model):
    Username=models.CharField(max_length=150)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    Block_no=models.CharField(max_length=150)
    Service_required=models.CharField(max_length=150)
    Askadmin=models.CharField(max_length=150)
    def __str__(self):
       return self.Username
    class Meta:
        db_table='authenticate_servicesofhostel'

class Notice(models.Model):
    Username=models.CharField(max_length=150)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    Block_no=models.CharField(max_length=150)
    Notice_from_admin=models.CharField(max_length=150)
    def __str__(self):
       return self.Username
class Msg_from_warden(models.Model):
    Username=models.CharField(max_length=150)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    Block_no=models.CharField(max_length=150)
    Wardenmsg=models.CharField(max_length=150)
    def __str__(self):
       return self.Username

class Complaint(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Room_no  = models.AutoField(primary_key=True)
    Room_no = models.IntegerField ()
    Block_no=models.CharField(max_length=150)
    Post_complaint=models.CharField(max_length=150)
    StudentPhonenumber= models.BigIntegerField ()
    Askadmin=models.CharField(max_length=150)
    def __str__(self):
       return self.Username






