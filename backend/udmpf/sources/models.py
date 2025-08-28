from django.db import models

from phonebook.models import Kontakt


class Source(models.Model):
    title = models.CharField(
        'Название',
        max_length=128,
    )
    description = models.CharField(
        'Описание',
        max_length=256,
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        Kontakt,
        on_delete=models.DO_NOTHING,
        related_name='Sources',
        verbose_name='Владелец информационного актива'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Информационный актив'
        verbose_name_plural = 'Информационные активы'

    def __str__(self):
        return self.title
