from django.contrib import admin
from blog.models import Link, Post, Script, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Script)
admin.site.register(Link)



