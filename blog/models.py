from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comments.count()  

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')  # Added related_name
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
