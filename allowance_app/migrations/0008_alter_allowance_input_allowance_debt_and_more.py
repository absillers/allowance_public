# Generated by Django 4.2.11 on 2024-06-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allowance_app', '0007_alter_allowance_input_allowance_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowance_input',
            name='allowance_debt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='allowance_input',
            name='allowance_no_debt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
