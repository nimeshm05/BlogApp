from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(help_text="Type your thoughts...")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, default='Random')
    favourite = models.CharField(max_length=25, default="Add one fav book...")

    def __str__(self):
        return self.title
        # Post.objects.raw('select title from Post')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

