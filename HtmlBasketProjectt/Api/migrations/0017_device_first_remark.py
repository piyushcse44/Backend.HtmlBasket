# Generated by Django 4.1.7 on 2023-05-02 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0016_alter_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='First_remark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_first_remark', to='vpn.remark'),
        ),
    ]