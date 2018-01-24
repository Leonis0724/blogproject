# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Post, Tag, Category

# Register your models here.


class CategoryInline(admin.TabularInline):
    # 关联到模型Category
    model = Category
    # 显示额外栏
    extra = 0


# class TagInline(admin.TabularInline):
#     # 关联到模型Tag
#     model = Tag
#     # 显示额外栏
#     extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [('作者标题', {'fields': ('author', 'title')}),
                 # ('日期时间', {'fields': ('created_time', 'modified_time')}),
                 ('日期时间', {'fields': ('created_time', )}),
                 ('分类标签', {'fields': ('category', 'tags')}),
                 ('文章正文', {'fields': ('excerpt', 'body')})]

    # inlines = [CategoryInline]
    # 过滤字段
    list_filter = ['title', 'author', 'created_time']


# 将模型注册到后台
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
