from django.shortcuts import render,redirect

from bloger.forms import EmployeeForm,AppointmentForm,CustomerForm,VehicleForm,ServiceForm,PaymentForm,InventoryForm
 
from bloger.models import Employee, ServicePack,Appointment,Vehicle,Payment,Inventory,Customer
def home_view(request):
    return render(request, 'home.html')
def contact_view(request):
    return render(request, 'contact.html')
def about_view(request):
    return render(request, 'about.html')
def services_view(request):
    return render(request, 'services.html')
def gallary_view(request):
    return render(request, 'gallary.html')
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
 
def appointment_view(request):
    if request.method == "POST":
        aform = AppointmentForm(request.POST)
        if aform.is_valid():
            aform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        aform = AppointmentForm()
    
    appointments = Appointment.objects.all()
    
    con = {
         'form1': AppointmentForm,
         'appointments':appointments
        
         ##'msg': message,
    }
    return render(request, "appointment.html", con)

def edit_appointment_view(request, AppointmentID):
    appointment = Appointment.objects.get(pk = AppointmentID)
    
    if request.method == "POST":
        
        appointmentform  = AppointmentForm(request.POST, instance = appointment)
         
        if appointmentform.is_valid():
            appointmentform.save()
            
    else:
               
        appointmentform = AppointmentForm(instance=appointment)
            
    con = {
        'g': appointment,
        'appointment': appointment
    }  
     
    return render(request, "edit_appointment.html", con)

def delete_appointment_view(request, AppointmentID):
    appointment = Appointment.objects.get(pk = AppointmentID)
    
    appointment.delete()
    
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
    
    return redirect(employee_view)     


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
        sform = EmployeeForm(request.POST)
        if sform.is_valid():
            sform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        sform = ServiceForm()
    
    
    services = ServicePack.objects.all()
    
    con = {
         ##'form4': ServiceForm,
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

def inventory_view(request):
    if request.method == "POST":
        iform = InventoryForm(request.POST)
        if iform.is_valid():
            iform.save()
            
            ##message = "DATA SAVES SUCCESSFULY"       
    else:
        
        iform = InventoryForm()
        
    inventory = Inventory.objects.all()
    
    con = {
         'form6': InventoryForm,
         'inventory': inventory
        
         ##'msg': message,
    }
    return render(request, "inventory.html", con)


def edit_inventory_view(request, ItemID):
    inventory = Inventory.objects.get(pk = ItemID)
    
    if request.method == "POST":
        
        inventoryform  = InventoryForm(request.POST, instance = inventory)
         
        if inventoryform.is_valid():
            
             inventoryform.save()
            
    else:
               
        inventoryform = InventoryForm(instance=inventory)
            
    con = {
        'g': inventoryform,
        'inventory': inventory
    }  
     
    return render(request, "edit_inventory.html", con)


def delete_inventory_view(request, ItemID):
    inventory = Inventory.objects.get(pk = ItemID)
    
    inventory.delete()
    
    return redirect(inventory_view)