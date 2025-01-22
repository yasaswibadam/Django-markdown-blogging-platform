from django.urls import re_path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView



urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/login/$', LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$', LoginView.as_view(), name='logout', kwargs={'next_page': '/'}),
    re_path(r'', include('blog.urls')),
]
