from django.contrib import admin

from .models import Comment
from blog.models import Post

# Register your models here.


class PostInline(admin.TabularInline):
    # 关联到模型Post
    model = Post
    # 显示额外栏
    extra = 0


class CommentAdmin(admin.ModelAdmin):
    # list_display = ['title', 'name', 'created_time', 'text']
    fieldsets = [('文章标题', {'fields': ('title',)}),
                 ('日期时间', {'fields': ('created_time',)}),
                 ('评论内容', {'fields': ('name', 'text')})]
    # inline
    # inlines = [PostInline]

    # 过滤字段
    list_filter = ['name', 'text']


admin.site.register(Comment, CommentAdmin)
