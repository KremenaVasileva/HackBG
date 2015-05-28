from django.conf.urls import url, patterns
from django.conf import settings

urlpatterns = patterns('webchat.views',
                       url(r'^$', 'index'),
                       url(r'^logged/$', 'logged'),
                       url(r'^home/$', 'home'),
                       url(r'^logout/$', 'logout_user'),
                       url(r'^post-message/$', 'post_message'),
                       )
