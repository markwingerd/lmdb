from django.conf.urls import include, url


urlpatterns = [
    url(r'^music/', include('music.urls', namespace='music')),
    # url(r'^admin/', include('admin.site.urls')),
]
