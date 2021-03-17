from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
# name이 만들어지면 slug필드가 자동으로 채워짐
admin.site.register(Category, CategoryAdmin)