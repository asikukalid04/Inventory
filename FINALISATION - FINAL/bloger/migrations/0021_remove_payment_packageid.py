# Generated by Django 4.2.6 on 2023-11-10 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0020_payment_packageid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='PackageID',
        ),
    ]