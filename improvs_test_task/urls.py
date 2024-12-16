from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for the Note-Taking app",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path('api/user/', include(('apps.user.urls', 'user'), namespace='user')),
    path('api/notes/', include(('apps.note.urls', 'note'), namespace='note')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api_docs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
