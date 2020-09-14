from django.contrib import admin
from blog.models import Link, Post, Script, Tag, Man, Command

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Script)
admin.site.register(Link)
admin.site.register(Man)
admin.site.register(Command)