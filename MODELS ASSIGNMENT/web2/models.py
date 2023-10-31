from django.db import models

class Employee(models.Model) :
  EmpName = models.CharField(max_length=20)
  EmpSex = models.CharField(max_length=20)
  EmpTitle = models.CharField(max_length=10)
  EmpDob = models.DateField (auto_now_add=False) 
  EmpStatus = models.CharField(max_length=10)
  EmpAddress = models.CharField(max_length=10, null=True)
  EmpContact = models.CharField(max_length=10)
  EmpEmail = models.EmailField()
  EmpQualfication = models.CharField(max_length=100)

class EquipmentCategory(models.Model):
  category_id = models.AutoField(primary_key=True)
  category_name = models.CharField(unique=True, max_length=45)
  category_description = models.TextField(blank=True, max_length=20)
  date_created = models.DateField(auto_now=True)
 
 
class products(models.Model):
  product_id = models.AutoField(primary_key=True)
  category_id = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)
  product_name = models.CharField(max_length=20)
  unit_price = models.IntegerField()
  sale_price = models.IntegerField()
  available_stock = models.IntegerField()
  unit_measure = models.IntegerField()
  date_updated = models.DateField()

class Transactions(models.Model):
  transaction_id = models.AutoField(primary_key=True)
  product_id = models.ForeignKey(products, on_delete=models.CASCADE)
  transaction_type = models.CharField(max_length=20)
  stock_taken = models.CharField(max_length=20)
  transaction_amount = models.IntegerField()
  transaction_date = models.DateField()