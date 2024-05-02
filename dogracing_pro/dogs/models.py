from django.db import models
from django.utils import timezone


class Dog(models.Model):
    class BreedsEnum(models.TextChoices):
        # Азавак
        # Афганская аборигенная собака
        # Венгерская борзая
        # Дирхаунд
        # Ирландский вольфхаунд
        # Испанская борзая
        # Малая итальянская борзая
        # Польская борзая
        # Русская псовая борзая
        # Салюки
        # Слюги
        # Тазы
        # Тайган
        # Уиппет
        # Хортая борзая
        # Южнорусская степная борзая
        # Басенджи
        # Фараонова собака
        # Мексиканская голая собака
        # Перуанская голая собака
        # Чернеко дель этна
        # Поденго ибиценко
        # Португальская поденго
        # Поденго канарио
        # Тайский риджбек
        # Родезийский риджбек
        pass
    
    class SexEnum(models.TextChoices):
        male = 'male'
        female = 'female'  
          
    name = models.CharField(max_length=150)
    breed = models.CharField(choices=BreedsEnum)
    birthday = models.DateField(default=timezone.now)
    sex = models.CharField(choices=SexEnum)
    tatoo = models.CharField(max_length=15)
    microchip_number = models.CharField(max_length=30)
    rkf_number = models.CharField(max_length=15)
    qualification_book_number = models.CharField(max_length=20)
    