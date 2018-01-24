from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .forms import CommentForm

import logging

# log
logger = logging.getLogger(__name__)

def post_comment(request, pk):
    # 根据文章pk把评论和被评论的文章关联起来,当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    post = get_object_or_404(Post, pk=pk)

    # HTTP 请求有 get 和 post 两种, 只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST（类字典对象形式）中，实例化表单。
        form = CommentForm(request.POST)

        # 当检查表单的数据是否符合格式要求。
        if form.is_valid():
            # commit=False 作用：利用表单数据生成 Comment 实例，暂时不保存评论数据到数据库。
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来。
            comment.post = post

            # 若检查到数据合法，调用表单的 save 方法保存数据到数据库
            comment.save()

            # 重定向到 post 的详情页：
            # 当 redirect 函数接收一个模型实例时，会调用 get_absolute_url 方法,
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)

        else:
            # 若数据不合法，重新渲染详情页，并且渲染表单的错误。
            # post.comment_set.all()：反向查询该篇 post 下的全部评论(Post和Comment 是 ForeignKey 关联)
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
            # 若不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)
