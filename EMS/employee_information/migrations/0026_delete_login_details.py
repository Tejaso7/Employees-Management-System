# Generated by Django 4.1.7 on 2023-09-27 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0025_login_hours_login_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login_Details',
        ),
    ]
