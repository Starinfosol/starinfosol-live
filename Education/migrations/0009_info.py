# Generated by Django 3.2.3 on 2021-06-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0008_remove_recruitment_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('cityName', models.CharField(max_length=255)),
            ],
        ),
    ]
