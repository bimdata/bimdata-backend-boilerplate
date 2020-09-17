from django.conf import settings
from django.urls import include
from django.urls import path


urlpatterns = []


if settings.ADMIN_INTERFACE == "True":
    from django.contrib import admin

    urlpatterns += [
        path("admin/", admin.site.urls, name="admin"),
        path("admin/doc/", include("django.contrib.admindocs.urls")),
    ]
