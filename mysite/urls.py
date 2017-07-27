from django.conf.urls import include, url
from django.contrib import admin
from theactualsite import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^art/$', views.artPage, name='artpage'),
    url(r'^programming/', views.programmingPage, name='programmingpage'),
    url(r'^art/(?P<artpiece_id>[0-9]+)$', views.piece_detail, name='piece_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
