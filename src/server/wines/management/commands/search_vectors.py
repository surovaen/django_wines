from django.contrib.postgres.search import SearchVector
from django.core.management import BaseCommand

from server.wines.models import Wine


class Command(BaseCommand):
    """Команда для обновления векторов поиска."""

    help = 'Обновление векторов поиска'

    def handle(self, *args, **options):
        """Консольный вывод."""
        self._update_search_vectors()
        self.stdout.write(
            'Векторы поиска обновлены.'
        )

    @staticmethod
    def _update_search_vectors():
        """Метод обновления векторов поиска моделей."""
        Wine.objects.update(
            name_vector=SearchVector('name'),
            description_vector=SearchVector('description'),
        )
