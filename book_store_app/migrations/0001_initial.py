# Generated by Django 5.0.6 on 2024-06-29 05:51

import book_store_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=book_store_app.models.filepath)),
            ],
        ),
    ]
