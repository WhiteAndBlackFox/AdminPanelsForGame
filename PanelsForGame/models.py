from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

# Добавляем дату до какого числа заблокирована учетка
class Profile(models.Model):
    user = models.CharField(max_length=20, help_text="Логин пользователя")
    passwd = models.CharField(max_length=20, null=True, help_text="Пароль пользователя")
    date_to_block = models.DateField(default=None, null=True, help_text="Дата окончания блокировки")

    def __str__(self):
        return '{}'.format(self.user)

# Фракции
class Fractions(models.Model):
    name = models.TextField(help_text="Наименование Фракции")
    count = models.IntegerField(default=0, help_text="Количество персонажей во фракции")

    def __str__(self):
        return '{}'.format(self.name)


# Персонаж
class Personage(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE, help_text="Индетефикатор пользователя")
    # user = models.IntegerField(default=1, null=True, help_text="Количество персонажей во фракции")
    nick_name = models.CharField(max_length=20, help_text="Имя персонажа", unique=True)
    fraction = models.ForeignKey(Fractions, default=None, on_delete=models.CASCADE, help_text="Индетефикатор фракции")
    date_create = models.DateTimeField(auto_now_add=True, help_text="Дата создание персонажа")
    date_last_input = models.DateTimeField(default=datetime.now(), help_text="Дата последнего входа")
    kill_count = models.PositiveIntegerField(default=0,  help_text="Счетсчик убийств")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.was_fraction = self.fraction_id

    def __str__(self):
        return '{}'.format(self.nick_name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.was_fraction is None:
            wc = Fractions.objects.get(id=self.was_fraction)
            Fractions.objects.filter(id=self.was_fraction).update(count=wc.count - 1)
        c = Fractions.objects.get(id=self.fraction_id)
        Fractions.objects.filter(id = self.fraction_id).update(count = c.count + 1)
        return super().save(force_insert, force_update, using, update_fields)

# Расположенеи предмета
class LocationGObject(models.Model):
    name = models.TextField(help_text="Место расположение объекта")

    def __str__(self):
        return '{}'.format(self.name)


# Тип патронов
class AmmoType(models.Model):
    name = models.TextField(help_text="Тип патронов")

# Группы предметов
class GroupGObject(models.Model):
    name = models.TextField(help_text="Тип предмета")
    location_gObject = models.ForeignKey(LocationGObject, on_delete=models.CASCADE,
                                            help_text="Расположение объекта в инвенторе")

# Предметы
class GameObjects(models.Model):
    name = models.TextField(null=False, help_text="Наименование объекта")
    lvl = models.PositiveIntegerField(null=False, blank = False, default=1, help_text="Уровень предмета")
    weight = models.FloatField(null=False, default=0.0, help_text="Вес предмет, кг")
    description = models.TextField(blank = True, help_text="Описание предмета")
    load_capacity = models.FloatField(blank = True, default=0, help_text="Грузоподъемность, кг")
    grouping = models.FloatField(blank = True, null=True, default=None, help_text="Кучность")
    fire_tempo = models.PositiveIntegerField(blank = True, null=True, default=None, help_text="Темп огня")
    ammo_type = models.OneToOneField(AmmoType, blank = True, null=True, on_delete=models.CASCADE, help_text="Тип патронов")
    group_game_object = models.ForeignKey(GroupGObject, on_delete=models.CASCADE, help_text="К какой группе принадлежат")

    def __str__(self):
        return '{}'.format(self.name)


# Инвентарь персонажа
class Inventory(models.Model):
    personage = models.ForeignKey(Personage,  default=0, on_delete=models.CASCADE, help_text="ИД персонажа")
    gObject = models.ForeignKey(GameObjects,  default=0, on_delete=models.CASCADE, help_text="ИД предмета")
    use_count = models.PositiveIntegerField(default=0, null=False, help_text="Кол-во использований")
    location_gObject = models.ForeignKey(LocationGObject, on_delete=models.CASCADE,
                                            help_text="Расположение объекта в инвенторе")

# Локации
class Locations(models.Model):
    name = models.TextField(null=False, help_text="Наименование локации")
    description = models.TextField(default=None, help_text="Описание локации")

    def __str__(self):
        return '{}'.format(self.name)


# Перемещение по локациям
class PersonageTransfer(models.Model):
    personage = models.ForeignKey(Personage, on_delete=models.CASCADE, help_text="ИД персонажа")
    locations = models.OneToOneField(Locations, on_delete=models.CASCADE, help_text="ИД локации")
    date_last_visit = models.DateTimeField(default=datetime.now(), help_text="Последняя дата визита локации")
