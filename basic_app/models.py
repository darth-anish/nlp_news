from django.db import models
from django.utils import timezone
from django.urls import reverse

# post model

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank = True, null=True)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
