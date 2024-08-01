# Generated by Django 4.2.11 on 2024-06-23 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allowance_app', '0006_alter_allowance_input_allowance_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowance_input',
            name='allowance_debt',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10000, null=True),
        ),
        migrations.AlterField(
            model_name='allowance_input',
            name='allowance_no_debt',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10000, null=True),
        ),
    ]
