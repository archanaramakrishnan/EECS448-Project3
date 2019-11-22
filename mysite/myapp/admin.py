from django.contrib import admin

from .models import Map
from .models import Post
from .models import Rate

# Register your models here.

admin.site.register(Map)
admin.site.register(Post)
admin.site.register(Rate)
