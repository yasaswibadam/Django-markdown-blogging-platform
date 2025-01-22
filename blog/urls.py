from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),

    re_path(r'^post/new/$', views.post_new, name='post_new'),

    re_path(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),

    re_path(r'^post/(?P<post_id>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^post/(?P<post_id>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<post_id>\d+)/remove/$', views.post_remove, name='post_remove'),

    re_path(r'^post/(?P<post_id>\d+)/comment/$', views.add_comment, name='add_comment'),

    re_path(r'^comment/(?P<comment_id>\d+)/remove/$', views.remove_comment, name='remove_comment'),
    re_path(r'^comment/(?P<comment_id>\d+)/approve/$', views.approve_comment, name='approve_comment'),
]
