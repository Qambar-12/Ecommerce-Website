# Generated by Django 5.0.6 on 2024-06-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.ImageField(default='uploads/categories/default.jpg', upload_to='uploads/categories/'),
        ),
    ]