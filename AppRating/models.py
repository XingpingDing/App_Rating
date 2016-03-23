from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class App(models.Model):
    appid = models.CharField(max_length=128, unique=True)
    appname = models.CharField(max_length=128)
    category = models.ForeignKey(Category, null=True)
    description = models.TextField()
    averscore = models.FloatField(default=0)
    commentcount = models.IntegerField(default=0)
    developer = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    iconpath = models.CharField(max_length=128)
    imagepath1 = models.CharField(max_length=128)
    imagepath2 = models.CharField(max_length=128)
    imagepath3 = models.CharField(max_length=128)
    viewcount = models.IntegerField(default=0)
    likecount = models.IntegerField(default=0)
    dislikecount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.appname

class Comment(models.Model):
    user = models.ForeignKey(User)
    app = models.ForeignKey(App, null=True)
    score = models.IntegerField(default=0)
    content = models.TextField()

    def __unicode__(self):
        return self.content