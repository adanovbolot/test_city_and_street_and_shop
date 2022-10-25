# Generated by Django 4.1.2 on 2022-10-25 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_address_address_city_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_rel', to='shop.address', verbose_name='Улица'),
        ),
    ]