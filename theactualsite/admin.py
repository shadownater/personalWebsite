from django.contrib import admin
from .models import Art, Programming, ArtImg, ProgImg

# Register your models here.
admin.site.register(Art)
admin.site.register(ArtImg)
admin.site.register(Programming)
admin.site.register(ProgImg)