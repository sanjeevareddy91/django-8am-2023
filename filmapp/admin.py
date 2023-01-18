from django.contrib import admin
from .models import Movies,People,Register_User
# Register your models here.

admin.site.register(Movies)
admin.site.register(People)
admin.site.register(Register_User)