# Generated by Django 3.1.2 on 2020-11-03 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GarmentsManagementApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='garment',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='garment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GarmentsManagementApp.garment'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=20)),
                ('CustomerPhn', models.CharField(max_length=12)),
                ('quantity', models.IntegerField()),
                ('TotalPrice', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GarmentsManagementApp.products')),
            ],
        ),
    ]