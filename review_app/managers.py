from django.db.models import QuerySet, Manager, Avg


class ReviewManager(Manager):

    def get_queryset(self):
        return QuerySet(self.model, using=self._db).all()


