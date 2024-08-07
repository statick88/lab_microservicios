# comments/models.py

from django.db import models

class Comment(models.Model):
    post_id = models.IntegerField()
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]
