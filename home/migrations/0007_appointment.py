# Generated by Django 3.2.3 on 2021-05-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=255)),
                ('information', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
