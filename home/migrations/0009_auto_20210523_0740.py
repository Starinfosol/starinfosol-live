# Generated by Django 3.2.3 on 2021-05-23 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
