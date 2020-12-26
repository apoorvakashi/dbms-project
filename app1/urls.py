from django.urls import path
import app1.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='login'),
    path('signup/', views.signupview, name='signup'),
    path('logout/', views.logoutview, name='logout'),
    path('vehicles/', views.vehicleview, name='vehicle'),
    path('hotels/', views.hotelview, name='hotel'),
    path('logs/', views.bookingsview, name='logs'),
    path('vbform/<int:id>/', views.vbformview, name='vbform'),
    path('hbform/<int:id>/', views.hbformview, name='hbform'),
    path('addvehicle/', views.addvehicle, name='addvehicle'),
    path('addhotel/', views.addhotel, name='addhotel'),
    path('deletevehicle/<int:id>/', views.deletevehicle, name='deletevehicle'),
    path('deletehotel/<int:id>/', views.deletehotel, name='deletehotel'),
    path('updatevehicle/<int:pk>/', views.VehicleUpdateView.as_view(), name='updatevehicle'),
    path('updatehotel/<int:pk>/', views.HotelUpdateView.as_view(), name='hotelvehicle'),
    path('vehiclehistory', views.vehiclehistoryview, name='vehiclehistory'),
    path('hotelhistory', views.hotelhistoryview, name='hotelhistory'),
]
