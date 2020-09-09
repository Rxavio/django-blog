from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Video)
admin.site.register(FileAdmin)

