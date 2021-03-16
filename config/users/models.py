from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """ Новые поля в модели пользователя"""
    second_name = models.CharField(max_length=150,
                                   blank=True,
                                   verbose_name='Отчество')
    phone = PhoneNumberField(unique=True,
                             verbose_name='Номер телефона',
                             null=True,
                             blank=True)
    birth_date = models.DateField(null=True,
                                  blank=True,
                                  verbose_name='Дата рождения')
    dormitory = models.ForeignKey('api.Dormitory',
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Общежитие')
    room = models.ForeignKey('api.Room',
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL,
                             verbose_name="Комната")
