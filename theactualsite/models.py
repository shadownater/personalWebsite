from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


#object for each piece of art
@python_2_unicode_compatible
class Art(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    madeWith = models.CharField(max_length=100)
    year = models.CharField(max_length=40)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Programming(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    madeWith = models.CharField(max_length=100)
    year = models.CharField(max_length=40)
    github = models.CharField(max_length=2000)
    contributors = models.CharField(max_length=1000) #for now
    completed = models.BooleanField()

    TYPE_CHOICES = (
        ('SCHOOL', 'School'),
        ('HOBBY', 'Hobby'),
    )

    type = models.CharField(
        max_length = 20,
        choices = TYPE_CHOICES,
        #default = 'SCHOOL',
    )


    def __str__(self):
        return self.title



# is there a way to combine these? FKs don't think so, not even with verb

# object for art images
class ArtImg(models.Model):
    id = models.AutoField(primary_key=True)
    myImg = models.ImageField(null=True, blank=True)
    associated_piece = models.ForeignKey(Art, on_delete=models.CASCADE)

# object for programming images
class ProgImg(models.Model):
    id = models.AutoField(primary_key=True)
    myImg = models.ImageField(null=True, blank=True)
    associated_piece = models.ForeignKey(Programming, on_delete=models.CASCADE)
