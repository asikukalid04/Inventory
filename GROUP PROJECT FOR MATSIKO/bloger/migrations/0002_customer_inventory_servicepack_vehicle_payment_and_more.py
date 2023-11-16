# Generated by Django 4.2.6 on 2023-11-05 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustomerID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Contact', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('ItemID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Quantity', models.CharField(max_length=20)),
                ('Unitprice', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Inventories',
            },
        ),
        migrations.CreateModel(
            name='ServicePack',
            fields=[
                ('PackageID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Servicepackages',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('VehhicleID', models.AutoField(primary_key=True, serialize=False)),
                ('Modal', models.CharField(max_length=20)),
                ('Licenseplate', models.CharField(max_length=4)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.customer')),
            ],
            options={
                'verbose_name_plural': 'Vehicles',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('TransactionID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.IntegerField()),
                ('PaymentMethod', models.CharField(max_length=20)),
                ('PaymentDate', models.DateField()),
                ('CusttomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.customer')),
            ],
            options={
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('Appointmrnt_ID', models.AutoField(primary_key=True, serialize=False)),
                ('AppointmentDate', models.DateTimeField(auto_now=True)),
                ('Status', models.CharField(max_length=20)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.customer')),
                ('ServiceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.servicepack')),
                ('VehicleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.vehicle')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]
