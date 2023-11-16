"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bloger.views import home_view, employee_view,about_view,services_view,gallary_view,contact_view,appointment_view,service_view,delete_employee_view,delete_appointment_view,delete_customer_view,delete_appointment_view,delete_inventory_view,delete_payment_view,delete_service_view,delete_vehicle_view,vehicle_view,payment_view,inventory_view,customer_view,edit_customer_view,edit_appointment_view,edit_employee_view,edit_inventory_view,edit_payment_view,edit_service_view,edit_vehicle_view

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path ('', home_view, name = 'home_page'),
    path ('about/', about_view, name = 'about_page'),
    path ('contact/', contact_view, name = 'contact_page'),
    path ('services/', services_view, name = 'services_page'),
    path ('gallary/', gallary_view, name = 'gallary_page'),
    path ('employee/', employee_view, name = 'employee_page'),
    path ('appointment/', appointment_view, name = 'appointment_page'),
    path ('service/', service_view, name = 'service_page'),
    path ('vehicle/', vehicle_view, name = 'vehicle_page'),
    path ('payment/', payment_view, name = 'payment_page'),
    path ('customer/', customer_view, name = 'customer_page'),
    path ('inventory/', inventory_view, name = 'inventory_page'),
    path ('edit_customer/<int:CustomerID>/', edit_customer_view, name = 'edit_customer_page'),
    path ('edit_appointment/<int:AppointmentID>/', edit_appointment_view, name = 'edit_appointment_page'),
    path ('edit_employee/<int:EmployeeID>/', edit_employee_view, name = 'edit_employee_page'),
    path ('edit_service/<int:PackageID>/', edit_service_view, name = 'edit_service_page'),
    path ('edit_payment/<int:TransactionID>/', edit_payment_view, name = 'edit_payment_page'),
    path ('edit_vehicle/<int:VehicleID>/', edit_vehicle_view, name = 'edit_vehicle_page'),
    path ('edit_inventory/<int:ItemID>/', edit_inventory_view, name = 'edit_inventory_page'),
    path ('delete_employee/<int:EmployeeID>/', delete_employee_view, name = 'delete_employee_page'),
    path ('delete_appointment/<int:AppointmentID>/', delete_appointment_view, name = 'delete_appointment_page'),
    path ('delete_customer/<int:CustomerID>/', delete_customer_view, name = 'delete_customer_page'),
    path ('delete_vehicle/<int:VehicleID>/', delete_vehicle_view, name = 'delete_vehicle_page'),
    path ('delete_service/<int:PackageID>/', delete_service_view, name = 'delete_service_page'),
    path ('delete_payment/<int:TransactionID>/', delete_payment_view, name = 'delete_payment_page'),
    path ('delete_inventory/<int:ItemID>/', delete_inventory_view, name = 'delete_inventory_page'),











   
]
