import uuid
from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False)
    priority = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['id', 'name', 'priority'])
        ]