from django.db import models


class City(models.Model):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Город"
        ordering = ('name',)

    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name


class Street(models.Model):
    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
        ordering = ('name',)

    name = models.CharField('Название', max_length=50)
    city = models.ForeignKey(City, verbose_name='Улица', on_delete=models.CASCADE, related_name='address_rel')

    def __str__(self):
        return self.name


class Shop(models.Model):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        ordering = ('name',)

    name = models.CharField('Название', max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', related_name='city_shop')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name='Улица', related_name='address_shop')
    home = models.CharField('Дом', max_length=50)
    opening_time = models.TimeField(verbose_name='Время открытия')
    closing_time = models.TimeField(verbose_name='Время закрытия')

    def __str__(self):
        return f"Название: {self.name}" \
               f"Адресс: {self.street}"
