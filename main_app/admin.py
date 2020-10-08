from django.contrib import admin
from .models import Lemur, Feeding, Toy

# Register your models here.
admin.site.register(Lemur)
admin.site.register(Feeding)
admin.site.register(Toy)
