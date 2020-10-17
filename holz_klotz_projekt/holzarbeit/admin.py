from django.contrib import admin
from .models import Holzarten, Brett, Scheiben, Holz

admin.site.register(Holzarten)
admin.site.register(Brett)
admin.site.register(Scheiben)
admin.site.register(Holz)