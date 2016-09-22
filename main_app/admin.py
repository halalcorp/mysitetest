from django.contrib import admin

from .models import Post, Country, Formation, School

# Register your models here.

admin.site.register(Post)
admin.site.register(Country)
admin.site.register(Formation)
admin.site.register(School)
