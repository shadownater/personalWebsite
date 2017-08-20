from django.conf.urls import include, url
from django.contrib import admin
from theactualsite import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^art/$', views.artPage, name='artpage'),
    url(r'^programming/$', views.programmingPage, name='programmingpage'),
    url(r'^art/(?P<artpiece_id>[0-9]+)$', views.piece_detail, name='piece_detail'),
    url(r'^programming/(?P<progpiece_id>[0-9]+)$', views.p_piece_detail, name='p_piece_detail'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


