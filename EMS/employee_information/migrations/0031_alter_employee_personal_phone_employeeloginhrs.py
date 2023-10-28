# Generated by Django 4.1.7 on 2023-10-03 12:11

from django.db import migrations, models
import django.db.models.deletion
import employee_information.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0030_alter_login_hours_active_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_personal',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.CreateModel(
            name='EmployeeLoginHrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('login_dtime', models.DateTimeField(null=True)),
                ('logout_dtime', models.DateTimeField(null=True)),
                ('break_start_dtime', models.DateTimeField(default=employee_information.models.default_start_time, null=True)),
                ('break_end_dtime', models.DateTimeField(default=employee_information.models.default_start_time, null=True)),
                ('session_time', models.CharField(max_length=500)),
                ('break_time', models.CharField(max_length=500)),
                ('active_time', models.CharField(max_length=500)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_information.employee_personal')),
            ],
        ),
    ]
