from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'
urlpatterns = [
    url(r'^posts/$', views.posts, name = 'posts'), #^ - начало строки $- конец строки
    url(r'^post/(?P<post_id>[0-9]+)$', views.posts, name = 'posts'), #?P - означает шаблон,  стандарт
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^api/posts/$', views.api_post, name = 'api_posts'),
    url(r'^api/post/$', views.api_post, name = 'api_post')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
