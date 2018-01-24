import markdown

from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse
from django.core.urlresolvers import reverse

from django.utils.html import strip_tags


# Create your models here.
class Category(models.Model):
    """
    类别:
    Django 所有模型必须继承 models.Model ,更深了解请查看官方文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tag"


class Post(models.Model):
    """
    文章
    """

    # 标题
    title = models.CharField(max_length=70)

    # 正文 TextField。
    body = models.TextField()

    # 创建时间
    created_time = models.DateTimeField()

    # 最后修改时间
    modified_time = models.DateTimeField(auto_now_add=True)

    # 文章摘要(可以为空，指定blank=True实现)但默认CharField 要求必须存入数据。
    excerpt = models.CharField(max_length=200, blank=True)

    # ForeignKey、ManyToManyField 可参考官方文档 https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    # 文章:类别 关系：N : 1 
    category = models.ForeignKey(Category)

    # 文章:标签 关系: N : M, 标签可为空 
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章:作者 关系: N : 1
    # User 是从django.contrib.auth.models导入的用户模型,
    #  Django内置用户验证的应用，专门用于处理网站用户注册,登录等流程
    author = models.ForeignKey(User)

    # 新增 views 字段: 记录阅读量
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        '''
        通过首次实例Post, 阅读量自增1; 然后通过save方法更新到数据库中.
        '''
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = "post"
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


class Suggest(models.Model):
    """
    意见存储
    """
    suggest = models.TextField('意见', max_length=200)
    suggest_time = models.DateTimeField('提出时间', auto_now_add=True)

    def __str__(self):
        return self.suggest

    class Meta:
        db_table = "suggest"
