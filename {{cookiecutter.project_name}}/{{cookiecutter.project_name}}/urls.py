from django.conf import settings
from django.urls import include
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

# For register a new viewset :
# router.register('new-view', NewViewSet)

urlpatterns = [path("", include(router.urls)), path("health/", include("health_check.urls"))]


if settings.ADMIN_INTERFACE == "True":
    from django.contrib import admin

    urlpatterns += [
        path("grappelli/", include("grappelli.urls")),
        path("admin/", admin.site.urls, name="admin"),
        path("admin/doc/", include("django.contrib.admindocs.urls")),
    ]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
