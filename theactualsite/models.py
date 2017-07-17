from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


#object for each piece of art - includes programming projects because they are art too!
@python_2_unicode_compatible
class artPiece(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    madeWith = models.CharField(max_length=100)
    year = models.CharField(max_length=40)

    img = [] #an array of the above objects - not sure how this will work but we'll see how it goes

    def __str__(self):
        return self.title

# object for images
class img(models.Model):
    myImg = models.ImageField(null=True, blank=True)
    associated_artPiece = models.ForeignKey(artPiece, on_delete=models.CASCADE)
