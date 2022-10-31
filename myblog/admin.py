from atexit import register
from django.contrib import admin
from myblog.models import Article
# Register your models here.



# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status','created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
admin.site.register(Article)

