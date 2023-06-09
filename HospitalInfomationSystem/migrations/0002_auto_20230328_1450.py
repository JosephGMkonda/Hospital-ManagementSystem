# Generated by Django 3.2 on 2023-03-28 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalInfomationSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmittedPatient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=20)),
                ('village', models.CharField(max_length=255)),
                ('diseases', models.CharField(max_length=255)),
                ('admitted', models.DateField(default=django.utils.timezone.now)),
                ('Bed_Number', models.IntegerField()),
                ('Ward_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OutPatient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=225)),
                ('Gender', models.CharField(max_length=20)),
                ('Village', models.CharField(max_length=250)),
                ('diseases', models.CharField(max_length=255)),
                ('visited', models.DateField(default=django.utils.timezone.now)),
                ('drugs', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
