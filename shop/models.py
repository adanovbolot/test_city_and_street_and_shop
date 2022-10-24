from django.db import models


class City(models.Model):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Город"
        ordering = ('name',)

    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name


class Address(models.Model):
    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
        ordering = ('name',)

    name = models.CharField('Название', max_length=50)
    address = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return self.name


class CityAndStreet(models.Model):
    address_f = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Адрес', related_name='address_rel')
    city_f = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', related_name='city_rel')


class Shop(models.Model):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        ordering = ('name',)

    name = models.CharField('Название', max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Улица')
    home = models.CharField('Дом', max_length=50)
    opening_time = models.TimeField('Время открытия')
    closing_time = models.TimeField('Время закрытия')

    def __str__(self):
        return f"Название: {self.name}" \
               f"Адресс: {self.address}"
