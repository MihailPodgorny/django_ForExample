from django.db import models


class Dormitory(models.Model):
    """
    Описание модели Общежитие.
    """
    number = models.IntegerField(verbose_name="Номер общежития", unique=True)
    faculty = models.CharField(max_length=255, verbose_name="Факультет", unique=True)
    number_of_floors = models.IntegerField(default=9, verbose_name="Количество этажей")
    number_of_rooms = models.IntegerField(default=100, verbose_name="Количество комнат")

    def __str__(self):
        return f"Общежитие №{self.number}"

    class Meta:
        verbose_name = 'Общежитие'
        verbose_name_plural = 'Общежития'


class Room(models.Model):
    """
    Описание модели Комната.
    """
    number = models.IntegerField(verbose_name="Номер комнаты", unique=True)
    floor = models.IntegerField(verbose_name="Этаж")
    number_of_beds = models.IntegerField(default=4, verbose_name="Количество спальных мест")
    dormitory = models.ForeignKey('Dormitory',
                                  default=1,
                                  verbose_name="Общежитие",
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f"Комната №{self.number}"

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
