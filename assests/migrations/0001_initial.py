# Generated by Django 4.2 on 2023-04-07 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0004_employeeinfo_full_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assests_name', models.CharField(max_length=50)),
                ('assests_type', models.CharField(choices=[('phones', 'Phones'), ('tablets', 'laptops'), ('laptops', 'laptops')], max_length=15)),
                ('assests_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('brand', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('assests_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HandedOutAssests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('provide_at', models.DateField(auto_now_add=True)),
                ('return_at', models.DateField()),
                ('present_condition', models.TextField()),
                ('return_condition', models.TextField()),
                ('handedout_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handedout_by', to=settings.AUTH_USER_MODEL)),
                ('handedout_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeeinfo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assests', to='assests.assests')),
            ],
        ),
    ]
