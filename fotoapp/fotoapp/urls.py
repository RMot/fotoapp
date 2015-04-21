from conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from fotoapp import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plataforma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^eventos/', include('eventos.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
