from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Тема', max_length=250)
    full_text = models.TextField('ПОСТ')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/news/{self.id}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'