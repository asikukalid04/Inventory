# Generated by Django 4.2.6 on 2023-10-31 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web2', '0008_rename_available_stock_products_available_stock_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='Product_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='Stock_type',
            new_name='stock_taken',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='Transaction_amount',
            new_name='transaction_amount',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='Transaction_date',
            new_name='transaction_date',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='Transaction_id',
            new_name='transaction_id',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='Transaction_Type',
            new_name='transaction_type',
        ),
    ]
