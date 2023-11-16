from django.forms import ModelForm
from bloger.models import Employee,Customer,ServicePack,Vehicle,Appointment,Inventory,Payment

class EmployeeForm(ModelForm):
    class Meta:
      model = Employee
      fields = '__all__'      
      
class CustomerForm(ModelForm):
    class Meta:
      model = Customer
      fields = '__all__'      

class ServiceForm(ModelForm):
    class Meta:
      model = ServicePack
      fields = '__all__'   
      
class VehicleForm(ModelForm):
    class Meta:
      model = Vehicle
      fields = '__all__'   

class AppointmentForm(ModelForm):
     class Meta:
      model = Appointment
      fields = '__all__' 
      
class InventoryForm(ModelForm):
    class Meta:
      model = Inventory
      fields = '__all__'   

class PaymentForm  (ModelForm):
    class Meta:
      model = Payment
      fields = '__all__'   
      