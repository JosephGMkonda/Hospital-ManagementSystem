# Generated by Django 3.2 on 2023-03-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalInfomationSystem', '0002_auto_20230328_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admittedpatient',
            name='Ward_Name',
        ),
        migrations.AddField(
            model_name='admittedpatient',
            name='drugs',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]
