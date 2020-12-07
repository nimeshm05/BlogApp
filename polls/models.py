from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poll(models.Model):
    question = models.TextField(unique=True)
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='Random')

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
