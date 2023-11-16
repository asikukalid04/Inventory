from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from django.http import HttpResponse
from bloger.forms import EmployeeForm,CustomerForm,VehicleForm,ServiceForm,PaymentForm
 
from bloger.models import Employee, ServicePack,Vehicle,Payment,Customer
def home_view(request):
    return render(request, 'home.html')
def contact_view(request):
    return render(request, 'contact.html')
def about_view(request):
    return render(request, 'about.html')
def services_view(request):
    return render(request, 'services.html')

def employee_view(request):
    if request.method == "POST":
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            empform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        empform = EmployeeForm()
        
    employees = Employee.objects.all()
         
    con = { 
         'form': EmployeeForm,
         'employees': employees,
        
         ##'msg': message,
    }
    return render(request, "employee.html", con)

def edit_employee_view(request, EmployeeID):
    employee = Employee.objects.get(pk = EmployeeID)
    
    if request.method == "POST":
        
        employeeform  = EmployeeForm(request.POST, instance = employee)
         
        if employeeform.is_valid():
            employeeform.save()
            
    else:
               
        employeeform = EmployeeForm(instance=employee)
            
    con = {
        'g': employeeform,
        'employee': employee,
    }  
     
    return render(request, "edit_employee.html", con)

def delete_employee_view(request, EmployeeID):
    employee = Employee.objects.get(pk = EmployeeID)
    
    employee.delete()
    
    return redirect(employee_view)
 

  
def customer_view(request):
    if request.method == "POST":
        cform = CustomerForm(request.POST)
        if cform.is_valid():
            cform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        cform = CustomerForm()
    
    customers = Customer.objects.all()
    
    con2 = {
         'form2': CustomerForm,
         'customers': customers
        
         ##'msg': message,
    }
    return render(request, "customer.html", con2)

def edit_customer_view(request, CustomerID):
    customer = Customer.objects.get(pk = CustomerID)
    
    if request.method == "POST":
        
        customerform  = CustomerForm(request.POST, instance = customer)
         
        if customerform.is_valid():
            customerform.save()
            
    else:
               
        customerform = CustomerForm(instance=customer)
            
    con = {
        'g': customerform,
        'customer': customer
    }  
     
    return render(request, "edit_customer.html", con)

   
def delete_customer_view(request, CustomerID):
    customer = Customer.objects.get(pk = CustomerID)
    
    customer.delete()
    
    return redirect(customer_view)     


def vehicle_view(request):
    if request.method == "POST":
        vform = VehicleForm(request.POST)
        if vform.is_valid():
            vform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        vform = VehicleForm()
    
    vehicles = Vehicle.objects.all()      
     
    con = {
         'form3': VehicleForm,
         'vehicles': vehicles
        
         ##'msg': message,
    }
    return render(request, "vehicle.html", con)

def edit_vehicle_view(request, VehicleID):
    vehicle = Vehicle.objects.get(pk = VehicleID)
    
    if request.method == "POST":
        
        vehicleform  = VehicleForm(request.POST, instance = vehicle)
         
        if vehicleform.is_valid():
            vehicleform.save()
            
    else:
               
        vehicleform = VehicleForm(instance = vehicle)
            
    con = {
        'g': vehicleform,
        'vehicle': vehicle,
    }  
     
    return render(request, "edit_vehicle.html", con)

def delete_vehicle_view(request, VehicleID):
    vehicle = Vehicle.objects.get(pk = VehicleID)
    
    vehicle.delete()
    
    return redirect(vehicle_view)

def service_view(request):
    if request.method == "POST":
        sform = ServiceForm(request.POST)
        if sform.is_valid():
            sform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        sform = ServiceForm()
    
    
    services = ServicePack.objects.all()
    
    con = {
         'form4': ServiceForm,
         'services': services
        
         ##'msg': message,
    }
    return render(request, "service.html", con)

def edit_service_view(request, PackageID):
    service = ServicePack.objects.get(pk = PackageID)
    
    if request.method == "POST":
        
        serviceform  = ServiceForm(request.POST, instance = service)
         
        if serviceform.is_valid():
            serviceform.save()
            
    else:
               
        serviceform = ServiceForm(instance=service)
            
    con = {
        'g': serviceform,
        'service': service,
    }  
     
    return render(request, "edit_service.html", con)

def delete_service_view(request, PackageID):
    service = ServicePack.objects.get(pk = PackageID)
    
    service.delete()
    
    return redirect(service_view)

def payment_view(request):
    if request.method == "POST":
        pform = PaymentForm(request.POST)
        if pform.is_valid():
            pform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        pform = PaymentForm()
        
    payments = Payment.objects.all()
    
    con = {
         'form5': PaymentForm,
         'payments': payments
        
         ##'msg': message,
    }
    return render(request, "payment.html", con)

def edit_payment_view(request, TransactionID):
    payment = Payment.objects.get(pk = TransactionID)
    
    if request.method == "POST":
        
        paymentform  = PaymentForm(request.POST, instance = payment)
         
        if paymentform.is_valid():
            paymentform.save()
            
    else:
               
        paymentform = PaymentForm(instance=payment)
            
    con = {
        'g': paymentform,
        'payment': payment
    }  
     
    return render(request, "edit_payment.html", con)

def delete_payment_view(request, TransactionID):
    payment = Payment.objects.get(pk = TransactionID)
    
    payment.delete()
    
    return redirect(payment_view)



def sign_up_view(request):
    if request.method == "POST":
        signform = UserCreationForm(request.POST)
        if signform.is_valid():
            signform.save()
    else:
        signform = UserCreationForm()
    
    con = {
        'form': signform
    }
    return render(request,'registration/signup.html', con)

def print_customer_view(request, CustomerID):
    customer = Customer.objects.get(pk = CustomerID)
    con = {
        'customer': customer
    }
    return render(request, 'print_customer.html', con)

def print_vehicle_view(request,    VehicleID):
    vehicle = Vehicle.objects.get(pk = VehicleID)
    con = {
        'vehicle': vehicle
    }
    return render(request, 'print_vehicle.html', con)

def print_service_view(request, PackageID):
    service = ServicePack.objects.get(pk = PackageID)
    con = {
        'service': service
    }
    return render(request, 'print_service.html', con)

def print_payment_view(request, TransactionID):
    payment = Payment.objects.get(pk = TransactionID)
    con = {
        'payment': payment
    }
    return render(request, 'print_payment.html', con)

def print_employee_view(request, EmployeeID):
    employee = Employee.objects.get(pk = EmployeeID)
    con = {
        'employee': employee
    }
    return render(request, 'print_employee.html', con)
