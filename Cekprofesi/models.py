from django.db import models

class Matkul(models.Model):

    matkul = models.CharField(max_length=50)
    slbmatkul = models.TextField(default=True)
    semester = models.CharField(max_length=1)
    def __str__(self):
        return "{}. {}".format(self.id,self.matkul)


class ProfMatkul(models.Model):
    profesi=models.CharField(max_length=50)
    matkul=models.CharField(max_length=50)
    presentase=models.CharField(max_length=4)
    katasama=models.TextField(default=True)
    def __str__(self):
        return "{}. {}".format(self.id,self.matkul)
        

class Profesi(models.Model):
   
    profesi = models.CharField(max_length=50)
    unitk = models.TextField(default=True)
    def __str__(self):
        return "{}. {}".format(self.id,self.profesi)

class Kursus(models.Model):

    kursus = models.CharField(max_length=50)
    slbkursus = models.TextField(default=True)
    semester = models.CharField(max_length=1)
    def __str__(self):
        return "{}. {}".format(self.id,self.kursus)

class ProfKursus(models.Model):
    profesi=models.CharField(max_length=50)
    kursus=models.CharField(max_length=50)
    presentase=models.CharField(max_length=4)
    katasama=models.TextField(default=True)
    def __str__(self):
        return "{}. {}".format(self.id,self.kursus)

    
    