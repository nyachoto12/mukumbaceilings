# Generated by Django 2.2.10 on 2020-06-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop_mail', '0004_auto_20200602_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
