from django.db import models

class Menu(models.Model):
    name = models.CharField(default=None, max_length=50)
    Type = models.CharField(default=None, max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    comment = models.TextField(default=None)
    score = models.IntegerField(default=None)

    def __str__(self):
        return self.menu
