from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment
from .models import Programacao


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Programacao)
