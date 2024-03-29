from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'blog'


urlpatterns = [
    path('', views.blogList.as_view(), name='blogListPage'),
    path('user/register', views.userCreate.as_view(), name = 'userRegisterPage'),
    path('user/login', auth_views.LoginView.as_view(template_name='blog/login.html'), name='loginPage'),
    path('user/logout', auth_views.logout_then_login, name='logoutPage'),
    path('createBlog',views.createBlog, name='blogCreatePage'),
    path('userBlogs', views.userBlogList.as_view(), name='userBlogListPage'),
    path('userDrafts', views.userDraftList.as_view(), name='userDraftListPage'),
    re_path(r'^display/(?P<pk>\d+)/$', views.displayBlog, name='blogDisplayPage'),
    re_path(r'^publish/(?P<pk>\d+)$', views.publishBlog, name='publishBlogPage'),
    re_path(r'^update/(?P<pk>\d+)$', views.updateBlog.as_view(), name='blogUpdatePage'),
    re_path(r'^delete/(?P<pk>\d+)$', views.deleteBlog.as_view(), name='blogDeletePage'),
    re_path(r'^aproveComment/(?P<pk>\d+)$', views.aproveComment, name='aproveCommentPage'),
    re_path(r'^deleteComment/(?P<pk>\d+)$', views.deleteComment.as_view(), name='deleteCommentPage'),
]
