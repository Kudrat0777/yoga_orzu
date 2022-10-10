from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    base = models.TextField()
    avatar = models.ImageField('Фото', upload_to='images/instructors')

    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструктора'
        db_table = 'instructor'