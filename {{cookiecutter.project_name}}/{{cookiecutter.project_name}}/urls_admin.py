from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("health/", include("health_check.urls")),
    path("grappelli/", include("grappelli.urls")),
    path("", admin.site.urls, name="admin"),
    path("doc/", include("django.contrib.admindocs.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
