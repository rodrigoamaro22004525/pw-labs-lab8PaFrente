from django.contrib import admin


from .models import *

# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Projetos)
admin.site.register(PontuacaoQuizz)