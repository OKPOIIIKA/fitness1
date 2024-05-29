from django.db import models

# Create your models here.
class Articles(models.Model):
   title = models.CharField('Название блога', max_length=50)
   anons = models.CharField('Анонс', max_length=250)
   full_text = models.TextField('Блог')
   date = models.DateTimeField('Дата публикации')

   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
       return f'/blogs/{self.id}'
   
   class Meta:
      verbose_name = 'Блог'
      verbose_name_plural = 'Блоги' 