from django.db import models

# Create your models here.
class Coaches(models.Model):
   name = models.CharField("Имя", max_length=50)
   title = models.CharField("Направление", max_length=50)
   activity = models.TextField("Описание")
   image = models.ImageField("Изображение", upload_to="coaches/")

   def __str__(self):
      return self.name
   
   class Meta:
      verbose_name = 'Тренер'
      verbose_name_plural = 'Тренеры' 

class Directions(models.Model):
   name = models.CharField("Название", max_length=50)
   desc = models.TextField("Описание")
   image = models.ImageField("Изображение", upload_to="directions/")

   def __str__(self):
      return self.name
   
   class Meta:
      verbose_name = 'Вид тренировок'
      verbose_name_plural = 'Виды тренировок'