from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from PIL import Image

class Biblio(models.Model):
    id_biblio = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    year = models.IntegerField()
    tip = models.CharField(max_length=50, default='')
    coll = models.CharField(max_length=250, default='')
    edition = models.CharField(max_length=250, default='')
    pages = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ('titre',)


class Sites(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    oper = models.CharField(max_length=250)
    sitename = models.CharField(max_length=500)
    infor = models.CharField(max_length=9000, default='')
    descr = models.CharField(max_length=9000, default='')
    site_logo = models.FileField(default='pasdimage.png')
    periode = models.CharField(max_length=300)
    coordx = models.FloatField()
    coordy = models.FloatField()
    paleol = models.CharField(max_length=300)
    bronze = models.CharField(max_length=30)
    discovered = models.IntegerField()
    iron = models.CharField(max_length=30)
    mesol = models.CharField(max_length=30)
    middle_age = models.CharField(max_length=30)
    neol1 = models.CharField(max_length=30)
    neol2 = models.CharField(max_length=30)
    neol3 = models.CharField(max_length=30)
    passport = models.CharField(max_length=20)
    topo = models.FileField(default='pasdimage.png')
    biblio = models.ManyToManyField(Biblio)

    def __str__(self):
        return self.sitename

    class Meta:
        ordering = ('sitename',)
        
    # def __str__(self):
    #     return f'{self.id}'  # user.username

    def get_absolute_url(self):
        return reverse('site-detail', kwargs={'pk':self.pk})


class Mobiliers(models.Model):
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)
    mob_nom = models.CharField(max_length=250)
    mob_logo = models.FileField(default='pasdimage.png')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.mob_nom

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.mob_logo.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.mob_logo.path)


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
