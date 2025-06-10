from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at_display')
    search_fields = ('title', 'content')

    def created_at_display(self, obj):
        return obj.create_at.strftime('%Y-%m-%d %H:%M')

# Register your models here.
