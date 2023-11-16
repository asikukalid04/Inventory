# Generated by Django 4.2.6 on 2023-11-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0009_rename_empqualfication_employee_empqualification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='EmpAddress',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpContact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpEmail',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpID',
            new_name='EmployeeID',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpName',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpSex',
            new_name='LastName',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpStatus',
            new_name='Role',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='EmpDob',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='EmpQualification',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='EmpTitle',
        ),
        migrations.AddField(
            model_name='employee',
            name='WorkShedule',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='PaymentDate',
            field=models.DateField(auto_now=True),
        ),
    ]