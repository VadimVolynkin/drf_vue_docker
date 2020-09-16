from django.db import models

class Car(models.Model):
    vendor = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    volume = models.PositiveSmallIntegerField()


# === Random Data Generator ========================================
# from random import *
# from string import *

# for _ in range(1000):
#     Car.objects.create(
#         vendor = ''.join(choice(ascii_letters) for _ in range(10)),
#         model = ''.join(choice(ascii_letters) for _ in range(10)),
#         year = randint(1956, 2020),
#         volume = randint(50, 8000),
#     )
# ==================================================================