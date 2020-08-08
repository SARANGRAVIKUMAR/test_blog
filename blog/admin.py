from django.contrib import admin
from .models import Blog,Category,Comment
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Blog, MyModelAdmin)
admin.site.register(Category)
admin.site.register(Comment)
