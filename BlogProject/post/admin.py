from django.contrib import admin
from .models import Post, Categories
# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author']
    class Meta:
        model = Post
        

admin.site.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    class Meta:
        model = Categories