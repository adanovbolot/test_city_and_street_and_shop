# Generated by Django 4.1.2 on 2022-10-25 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_cityandaddress_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.city', verbose_name='Улица'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CityAndAddress',
        ),
    ]
