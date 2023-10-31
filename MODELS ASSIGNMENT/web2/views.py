from django.shortcuts import render
from web2.forms import EmployeeForm
from web2.models import Employee
def home_view(request):
    return render(request,'home.html')
def contact_view(request):
    return render(request,'contact.html')
def emp_view(request):
    if request.method == "POST":
        empform = EmployeeForm(request.POST)
        if empform.is_valid():
            empform.save()
    else:
         empform = EmployeeForm()
    con = {
          'form': EmployeeForm,    
            }
    return render(request,'emp.html', con)

