# Generated by Django 4.2 on 2023-04-07 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_designationinfo_designation_of'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designationinfo',
            name='description',
        ),
    ]
