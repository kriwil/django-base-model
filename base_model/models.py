import uuid

from django.db import models
from django.utils import timezone


class BaseQuerySet(models.QuerySet):
    """
    Base queryset for BaseModel

    add remove method, to set queryset to removed
    """
    def remove(self):
        return self.filter(is_removed=False).update(is_removed=True, removed_time=timezone.now())


class BaseManager(models.Manager):
    """
    Base manager for BaseModel

    only fetch the non removed objects
    """
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db).filter(is_removed=False)


class BaseModel(models.Model):
    """
    Base model for all other models

    use UUID for primary key, add created_time, modified_time, is_removed,
    and removed_time
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField(default=timezone.now)

    is_removed = models.BooleanField(default=False)
    removed_time = models.DateTimeField(blank=True, null=True)

    all_objects = models.Manager()
    objects = BaseManager()

    class Meta:
        abstract = True

    def remove(self):
        self.is_removed = True
        self.removed_time = timezone.now()
        self.save()
