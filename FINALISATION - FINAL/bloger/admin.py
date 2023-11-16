from django.contrib import admin
 
from bloger.models import Employee,Customer,ServicePack,Payment,Vehicle

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ( "EmployeeID","FirstName","LastName","Address","Contact","Email","WorkShedule" )  
    list_filter = ( "EmployeeID","FirstName","LastName","Address","Contact","Email","WorkShedule" )
    search_fields = ( "EmployeeID","FirstName","LastName","Address","Contact","Email","WorkShedule" )
admin.site.register(Employee, EmployeeAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = (  "CustomerID","FirstName","LastName","Contact","Email","Address")  
    list_filter = (  "CustomerID","FirstName","LastName","Contact","Email","Address")
    search_fields =(  "CustomerID","FirstName","LastName","Contact","Email","Address")
admin.site.register(Customer, CustomerAdmin)

class VehicleAdmin(admin.ModelAdmin):
    list_display = (  "VehicleID","Modal","Licenseplate","CustomerID")
    list_filter = (  "VehicleID","Modal","Licenseplate","CustomerID")
    search_fields = (  "VehicleID","Modal","Licenseplate","CustomerID")
admin.site.register(Vehicle, VehicleAdmin)

class ServicePackAdmin(admin.ModelAdmin):
    list_display = (  "PackageID","Name","Description","Price")  
    list_filter = (  "PackageID","Name","Description","Price")  
    search_fields = (  "PackageID","Name","Description","Price")  
    sortable_by = (  "PackageID","Name","Description","Price")
    show_full_result_count = (  "PackageID","Name","Description","Price")
    sortfield_by = ( "Price")
admin.site.register(ServicePack, ServicePackAdmin)

class paymentAdmin(admin.ModelAdmin):
    list_display = (  "TransactionID","Amount","PaymentMethod","PaymentDate","PackageID","CustomerID")  
    list_filter = (  "TransactionID","Amount","PaymentMethod","PaymentDate","PackageID","CustomerID") 
    search_fields = (  "TransactionID","Amount","PaymentMethod","PaymentDate","PackageID","CustomerID") 
admin.site.register(Payment, paymentAdmin)









