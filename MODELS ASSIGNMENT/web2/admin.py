from django.contrib import admin
from web2.models import Employee,EquipmentCategory,products,Transactions

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (  "EmpName","EmpSex","EmpTitle","EmpDob","EmpStatus","EmpAddress","EmpContact","EmpEmail","EmpQualfication" )  
admin.site.register(Employee, EmployeeAdmin)

class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id","category_name","category_description","date_created")  
admin.site.register(EquipmentCategory,EquipmentCategoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("product_id","category_id","product_name","unit_price","sale_price","available_stock","unit_measure","date_updated")  
admin.site.register(products, ProductsAdmin)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("transaction_id","product_id","transaction_type","stock_taken","transaction_amount","transaction_date")  
admin.site.register(Transactions,TransactionsAdmin)
