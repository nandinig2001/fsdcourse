from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.db import models

# Create your models here.
class Assignment(models.Model):
    name = models.CharField(max_length=100)
    g1 = models.CharField(max_length=100)
    w1= models.CharField(max_length=100)
    g2 = models.CharField(max_length=100)
    w2 = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Page(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pfname=models.CharField(max_length=200)
    plname=models.CharField(max_length=200)
    pcollege=models.CharField(max_length=200)
    pmobile=models.IntegerField()
    page=models.IntegerField()

class Topic(models.Model):
    topicName = models.CharField(max_length=40)

    def _str_(self):
        return self.topicName

class Video(models.Model):
    videoid = models.CharField(max_length=40,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, null=True)
    topicName = models.CharField(max_length=40, null=True )
    url = EmbedVideoField()

    def __str__(self):
        return self.title


class Aquestions(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    p1 = models.CharField(max_length=800)
    p2= models.CharField(max_length=800)

    def __str__(self):
        return self.subject

class Quizz(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

    def _str_(self):
        return self.question

class FilesAdmin(models.Model):
    adminupload=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)
    imageurl = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
