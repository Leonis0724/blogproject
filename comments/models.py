from django.db import models


# Create your models here.
class Comment(models.Model):
    # 昵称
    name = models.CharField(max_length=100)
    # 邮箱
    email = models.EmailField(max_length=255)
    # URL
    url = models.URLField(blank=True)
    # 评论
    text = models.TextField()
    # 创建日期
    created_time = models.DateTimeField(auto_now_add=True)
    # 相关文章
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:30]

    class Meta:
        # 表名
        db_table = 'comment'
