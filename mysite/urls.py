from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^core/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
]
