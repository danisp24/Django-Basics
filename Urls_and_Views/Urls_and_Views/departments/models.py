from django.db import models
from django.utils.text import slugify


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,
                            unique=True,
                            blank=True)

    def __str__(self):
        return f" The ID is: {str(self.pk)} and the name is: {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
