from django.contrib import admin
from app1.models import Vehicle, VehicleBookings, Hotel, HotelBooking, UserExtend, VehicleHistory, HotelHistory

admin.site.register(Vehicle)
admin.site.register(VehicleBookings)
admin.site.register(Hotel)
admin.site.register(HotelBooking)
admin.site.register(UserExtend)
admin.site.register(VehicleHistory)
admin.site.register(HotelHistory)
