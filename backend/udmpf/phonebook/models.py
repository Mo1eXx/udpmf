from django.db import models


class Subdivision(models.Model):
    title = models.CharField(
        'Подразделение',
        max_length=128
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок вывода',
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ('-output_order',)

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(
        'Отдел',
        max_length=128
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок вывода'
    )

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ('-output_order',)

    def __str__(self):
        return self.title


class Kontakt(models.Model):
    last_name = models.CharField(
        'Фамилия',
        max_length=128
    )
    name = models.CharField(
        'Имя',
        max_length=128
    )
    s_name = models.CharField(
        'Отчество',
        max_length=128, blank=True, null=True
    )
    job_title = models.CharField(
        'Должность',
        max_length=128
    )
    ip_number = models.IntegerField(
        'Стационарный Телефон',
        blank=True, null=True
    )
    phone_number = models.CharField(
        'Мобильный Номер',
        unique=True,
        max_length=64, blank=True, null=True
    )
    e_mail = models.EmailField(
        'Почта',
        unique=True,
        max_length=64, blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='kontakt_department', verbose_name='Отдел'
    )
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='kontakt_subdivision', verbose_name='Подразделение'
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок вывода'
    )

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        constraints = (
            models.UniqueConstraint(
                fields=('last_name', 'name', 's_name'),
                name='Unique kontakt constraint',
            ),
        )

    def __str__(self):
        return f'{self.last_name} {self.name} {self.s_name}'
