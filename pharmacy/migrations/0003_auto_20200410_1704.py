# Generated by Django 3.0.5 on 2020-04-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_auto_20200410_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='image',
            field=models.ImageField(default='static/img/no_image.webp', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='image',
            field=models.ImageField(default='static/img/no_image.webp', upload_to='img/'),
        ),
    ]