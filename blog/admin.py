from django.contrib import admin
from .models import Category, Article, Event, SubCom,SubCom
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields= ('author','created_at','updated_at')
    search_fields = ('title', 'content', 'categories__name')
    list_display = ('title', 'author','public', 'created_at')
    list_filter = ('public', 'author', 'categories__name')

   

class EventAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at',)
    list_display = ('title', 'fecha')
    search_fields = ('title', 'description','fecha')

class SubCoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')




admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SubCom, SubCoAdmin)

