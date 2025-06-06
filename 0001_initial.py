# Generated by Django 5.2 on 2025-05-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
