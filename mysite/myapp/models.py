from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestion(models.Model):
    suggestion = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + " " + self.suggestion

class Comment(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + " " + self.comment
