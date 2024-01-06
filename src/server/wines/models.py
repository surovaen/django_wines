from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models


class WineMarket(models.Model):
    """Модель виномаркета."""

    name = models.CharField(
        'Наименование',
        max_length=255,
    )
    city = models.CharField(
        'Город',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Виномаркет'
        verbose_name_plural = 'Виномаркеты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Wine(models.Model):
    """Модель вина."""

    name = models.CharField(
        'Наименование',
        max_length=255,
    )
    name_vector = SearchVectorField(null=True)
    country = models.CharField(
        'Страна',
        max_length=255,
    )
    price = models.PositiveIntegerField(
        'Цена',
    )
    bottling_date = models.DateField(
        'Дата розлива',
    )
    description = models.TextField(
        'Описание',
        max_length=1000,
        null=True,
        blank=True,
    )
    description_vector = SearchVectorField(null=True)
    markets = models.ManyToManyField(
        WineMarket,
        verbose_name='Маркеты',
        through='WineMarketStock',
    )

    class Meta:
        verbose_name = 'Вино'
        verbose_name_plural = 'Вина'
        ordering = ('name',)
        indexes = (
            GinIndex(fields=('name_vector',)),
            GinIndex(fields=('description_vector',)),
        )

    def __str__(self):
        return self.name


class WineMarketStock(models.Model):
    """Связанная модель ассортимента вин в маркетах."""

    wine = models.ForeignKey(
        Wine,
        verbose_name='Вино',
        on_delete=models.CASCADE,
        related_name='wines',
    )
    market = models.ForeignKey(
        WineMarket,
        verbose_name='Маркет',
        on_delete=models.CASCADE,
        related_name='markets',
    )
    in_stock = models.BooleanField(
        'В наличии',
        default=False,
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Наличие вин в маркетах'
        ordering = ('in_stock',)
        constraints = (
            models.UniqueConstraint(
                fields=('wine', 'market'),
                name='unique_record',
            ),
        )

    def __str__(self):
        return f'Запись {self.pk}'
