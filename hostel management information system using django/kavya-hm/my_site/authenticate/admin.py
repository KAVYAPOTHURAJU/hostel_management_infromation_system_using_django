from django.contrib  import admin
from authenticate.models import Commentsinfo, BookingForm, Availability_room,DetailsofStudent,OutingFormforstudents, Visitor,Adminuser,RoomPaymentForm,MessPaymentForm,ServicesOfHostel,Notice,Msg_from_warden,Complaint
admin.site.register(BookingForm)
admin.site.register(Availability_room)
admin.site.register(DetailsofStudent)
admin.site.register(Commentsinfo)
admin.site.register(OutingFormforstudents)
admin.site.register(Visitor)
admin.site.register(Adminuser)
admin.site.register(RoomPaymentForm)
admin.site.register(ServicesOfHostel)
admin.site.register(MessPaymentForm)
admin.site.register(Notice)
admin.site.register(Msg_from_warden)
admin.site.register(Complaint)