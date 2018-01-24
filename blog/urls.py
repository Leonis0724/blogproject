from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # 根据关键词搜索
    # url(r'^search/$', views.search, name='search'),
    # 点击 '关于' 返回相关信息(前段页面有问题)
    #url(r'^about_me/$', views.suggest_view, name='about_me'),
    # 关于
    url(r'^aboutme/$', views.about, name='about'),
]
