# Generated by Django 4.1.7 on 2023-05-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0017_device_first_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='First_remark',
            field=models.CharField(default='', max_length=200),
        ),
    ]
