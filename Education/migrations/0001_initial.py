# Generated by Django 3.2.3 on 2021-05-31 10:54

import ckeditor.fields
import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('author', models.CharField(max_length=14)),
                ('tags', models.CharField(choices=[('Technology', 'Technology'), ('Health service', 'Health service'), ('Education', 'Education'), ('Others', 'Others')], default='Technology', max_length=100)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
