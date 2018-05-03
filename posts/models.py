from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField,Model

# from django_mysql.models import ListTextField

#kol mara bnghyr flmodel lazm n3ml migrate
# Create your models here.
class Post(models.Model):
    slug =models.SlugField()
    body =models.TextField() #textfield da haga twela
    date =models.DateTimeField(auto_now_add=True) #elfunction eligowa de bt2olo awel m tbd2 hot el date wltime bta3 dlw2ty
    thumb=models.ImageField(default='download.jpg' ,blank=True)
    author=models.ForeignKey(User,
    on_delete=models.CASCADE,default=None)
    # likes=models.ManyToManyField("self",symmetrical=False)
    # likes=models.ListTextField(base_field=IntegerField(), size=100,),

    def __str__(self):
        return self.slug
    # def snippet(self):
    #     return self.body[:50] +'...'
    # likes = []
    # likescount = 0
    # def AddLike(self):
    #     #model=models.Post
    #     likes.append('Mona')
    #     likescount+=1
