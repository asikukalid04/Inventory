from django.db import models

class Employee(models.Model) :
      EmployeeID = models.AutoField(primary_key=True)
      FirstName = models.CharField(max_length=200)
      LastName = models.CharField(max_length=200)
      Address = models.CharField(max_length=100, null=True)
      Role = models.CharField(max_length=100)
      Contact = models.CharField(max_length=100)
      Email = models.EmailField()
      WorkShedule = models.CharField(max_length=200)
      class Meta:
        verbose_name_plural = "Employees"
def __str__(self):
        return self.Employee_name
  
class Customer(models.Model):
      CustomerID = models.AutoField(primary_key=True)
      FirstName = models.CharField(max_length=200)
      LastName = models.CharField(max_length=200)
      Contact = models.CharField(max_length=200)
      Email = models.EmailField(max_length=254)
      Address = models.CharField(max_length=200) 
      class Meta:
            verbose_name_plural = "Customers"
def __str__(self):
      
        return self.Customer_name
  
class ServicePack(models.Model):
      PackageID = models.AutoField(primary_key=True)
      Name = models.CharField(max_length=200)
      Description = models.CharField(max_length=200)
      Price = models.IntegerField()
      class Meta:
            verbose_name_plural = "Servicepackages"
def __str__(self):
      
        return self.Servicepackage_name
  
class Vehicle(models.Model):
      VehicleID = models.AutoField(primary_key=True)
      Modal = models.CharField(max_length=200)
      Licenseplate = models.CharField(max_length=400)
      CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
      class Meta:
            verbose_name_plural = "Vehicles"
def __str__(self):
      
        return self.Vehicle_name
      
class Appointment(models.Model):
      AppointmentID = models.AutoField(primary_key=True)
      CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
      VehicleID = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
      PackageID = models.ForeignKey(ServicePack, on_delete=models.CASCADE)   
      AppointmentDate = models.DateField(auto_now = False)
      AppointmentTime = models.CharField(max_length=200)

      class Meta:
            verbose_name_plural = "Appointments"
def __str__(self):
      
        return self.Appointment_name

class Inventory(models.Model):
      ItemID = models.AutoField(primary_key=True)
      Name = models.CharField(max_length=200)
      Quantity = models.CharField(max_length=200)
      UnitPrice = models.IntegerField()
      class Meta:
            verbose_name_plural = "Inventories"
def __str__(self):
      
        return self.Invemtory_name  


class Payment(models.Model):
      TransactionID = models.AutoField(primary_key=True)
      Amount = models.IntegerField()
      PaymentMethod = models.CharField(max_length=200)
      PaymentDate = models.DateField(auto_now=True)
      CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
      class Meta:
            verbose_name_plural = "Payments"
def __str__(self):
      
        return self.Payment_name  

      
      

