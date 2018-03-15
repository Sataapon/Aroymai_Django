from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    voted = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    average = models.IntegerField(default=0)

    def vote(self, score):
        self.voted += 1
        self.total_score += score
        self.average = self.total_score/self.voted

class Comment(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
