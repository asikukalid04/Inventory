# Generated by Django 4.2.6 on 2023-11-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0010_rename_empaddress_employee_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Status',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='AppointmentDate',
            field=models.DateField(),
        ),
    ]