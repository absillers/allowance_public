# Generated by Django 4.2.11 on 2024-06-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allowance_app', '0011_alter_allowance_app_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowance_app',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True),
        ),
    ]
