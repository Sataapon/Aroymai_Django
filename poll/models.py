from django.db import models

class Menu(models.Model):
    name = models.CharField(default = None, max_length = 50)
    Type = models.CharField(default = None, max_length = 50)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(default = None, max_length = 50)

    def __str__(self):
        return self.name

class CommentScore(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.TextField(null = True)
    score = models.IntegerField(null = True)
