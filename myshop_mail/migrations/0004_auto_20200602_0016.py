# Generated by Django 2.2.10 on 2020-06-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop_mail', '0003_auto_20200601_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]