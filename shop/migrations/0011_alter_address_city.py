# Generated by Django 4.1.2 on 2022-10-25 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_city_address_address_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_rel', to='shop.city', verbose_name='Улица'),
        ),
    ]