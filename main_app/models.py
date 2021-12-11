from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(("Date"),default=datetime.date.today)
    
    
    def __str__(self):
        return self.title