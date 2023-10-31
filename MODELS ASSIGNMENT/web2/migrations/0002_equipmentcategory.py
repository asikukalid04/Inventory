# Generated by Django 4.2.6 on 2023-10-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=45, unique=True)),
                ('category_description', models.TextField(blank=True)),
                ('date_created', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Equipment Categories',
            },
        ),
    ]