# Generated by Django 3.1.2 on 2020-12-07 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GarmentsManagementApp', '0010_remove_employee_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GarmentsManagementApp.department'),
        ),
    ]