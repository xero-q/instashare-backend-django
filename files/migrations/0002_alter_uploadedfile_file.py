# Generated by Django 5.1.1 on 2024-09-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(max_length=255, upload_to='uploads/'),
        ),
    ]