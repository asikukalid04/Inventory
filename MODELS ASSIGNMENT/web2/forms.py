from django.forms import ModelForm


from web2.models import Employee
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'