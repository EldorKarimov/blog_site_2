from django.contrib import admin

from blog.models import blog, category, tag, comment

@admin.register(category.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":['name']}

@admin.register(tag.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":['name']}

@admin.register(blog.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug":['title']}

@admin.register(comment.Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'created']