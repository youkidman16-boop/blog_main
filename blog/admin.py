# -*- coding: utf-8 -*-

from.models import Post,Category,Comment
from django.contrib import admin
from.models import Post,Category,Comment

class CommentItemInline(admin.TabularInline):
    model=Comment
    raw_id_fields=['post']

class PostAdmin(admin.ModelAdmin):
        search_fields= ['title','intro','body']
<<<<<<< HEAD
        list_display=('title','category','created_at','Status')
        list_filter= ['category','created_at','Status']
=======
        list_display=('title','category','created_at','status')
        list_filter= ['category','created_at','status']
>>>>>>> dbe40ec4773845606f85831f788f85f3aea66215
        inlines= [CommentItemInline]

class CategoryAdmin(admin.ModelAdmin):
      search_fields=['title']
      list_display=('title',)

class CommentAdmin(admin.ModelAdmin):
      list_display=('name','post','created_at',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
