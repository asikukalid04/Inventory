# Generated by Django 4.2.6 on 2023-11-09 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0017_appointment_appointmenttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('SummaryID', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.customer')),
                ('PackageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.servicepack')),
                ('TransactionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.payment')),
                ('VehicleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloger.vehicle')),
            ],
            options={
                'verbose_name_plural': 'Summary',
            },
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='CustomerID',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='PackageID',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='VehicleID',
        ),
        migrations.DeleteModel(
            name='inventory',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
