from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Sites(models.Model):
    id_site = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    sitename = models.CharField(max_length=500)
    oper = models.CharField(max_length=250)
    descr = models.CharField(max_length=9000, default='')
    site_img = models.FileField(default='pasdimage.png')
    date = models.CharField(max_length=300)

    def __str__(self):
        return self.sitename

    # def __str__(self):
    #     return f'{self.id}'  # user.username
    
    class Meta:
        ordering = ('sitename',)

    def get_absolute_url(self):
        return reverse('site-detail', kwargs={'pk':self.pk})


class Mobiliers(models.Model):
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)
    mob_nom = models.CharField(max_length=250)
    mob_img = models.FileField(default='pasdimage.png')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.mob_nom

class Admini(models.Model):
    id_admini = models.IntegerField(primary_key=True)
    categ = models.CharField(max_length=250)
    vid = models.CharField(max_length=100)
    vid_comm = models.CharField(max_length=250)
    utilisation = models.CharField(max_length=250)
    herit = models.CharField(max_length=50)
    infor = models.CharField(max_length=9000, default='') # à supprimer vue qu'on a ces champs dans le table Sites
    descr = models.CharField(max_length=9000, default='') # à supprimer vue qu'on a ces champs dans le table Sites
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_admini


class Staticmap(models.Model):
    id_map = models.IntegerField(primary_key=True)
    mapname = models.CharField(max_length=250)
    mapfile = models.FileField()
    autor = models.CharField(max_length=250)

    def __str__(self):
        return self.mapname


class Images(models.Model):
    id_img = models.IntegerField(primary_key=True)
    imgname = models.CharField(max_length=250)
    imgfile = models.FileField(default='')
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.imgname
