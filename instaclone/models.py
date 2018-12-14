from django.db import models
from django.contrib.auth.models import User
# from tinymce.models import HTMLField
# from django.db.models import Q

Gender=(
    ('Male','Male'),
    ('Female','Female'),
)
# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()
