# Generated by Django 3.2 on 2023-03-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalInfomationSystem', '0003_auto_20230330_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admittedpatient',
            name='Bed_Number',
            field=models.CharField(max_length=5),
        ),
    ]
