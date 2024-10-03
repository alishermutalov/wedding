from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Wedding Invation API",
        default_version='v0.0.1',
        description="API documentation for Wedding Invation",
        contact=openapi.Contact(email="amutalov001@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/event/', include('event_api.urls')),
    path('api/gallery/', include('gallery_api.urls')),
    path('api/guests/', include('guest.urls')),
    path('api/subscription/', include('subscription.urls')),
    path('api/wedding/', include('wedding_api.urls')),
    path('api/payment/', include('payment.urls')),
    #documnetation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


