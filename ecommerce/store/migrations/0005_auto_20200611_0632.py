# Generated by Django 3.0.7 on 2020-06-11 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200611_0631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
