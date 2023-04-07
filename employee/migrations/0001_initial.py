# Generated by Django 4.2 on 2023-04-07 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50, unique=True)),
                ('department', models.CharField(choices=[('HR', 'Human Resource'), ('administrative', 'Administrative'), ('software development', 'Software Development'), ('QA', 'Quality Assurance'), ('project management', 'Project Management'), ('product panagement', 'Product Management'), ('design', 'Design'), ('devOps', 'DevOps'), ('customer support', 'Customer Support'), ('marketing', 'Marketing'), ('IT', 'Information Technology')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('employee_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('national_id', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('signature', models.ImageField(blank=True, upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('employee_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_company', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.designationinfo')),
            ],
        ),
    ]
