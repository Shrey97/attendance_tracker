from django.conf.urls import url, include
from django.contrib import admin
from attd.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', profile),
    url(r'markattendance', mark_attn),
    url(r'\w+/(?P<roll>\d+)$', mark_att_st),
    url(r'^edit_profile/$', edit_profile ,name='editprof'),
    url(r'^attendance_submit/$', attendance_done),
]
from django.views.generic import RedirectView
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/accounts/login/', permanent=True)),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_rot = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
