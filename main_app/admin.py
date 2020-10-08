from django.contrib import admin
from .models import Lemur, Feeding, Toy, Photo

# Register your models here.
admin.site.register(Lemur)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)