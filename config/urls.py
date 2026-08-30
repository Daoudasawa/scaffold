from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    path("api/v1/auth/", include("apps.accounts.urls")),
    path("api/v1/", include("apps.farms.urls")),
    path("api/v1/", include("apps.flocks.urls")),
    path("api/v1/", include("apps.monitoring.urls")),
    path("api/v1/", include("apps.mortality.urls")),
    path("api/v1/", include("apps.observations.urls")),
    path("api/v1/", include("apps.health.urls")),
    path("api/v1/", include("apps.alerts.urls")),
    path("api/v1/", include("apps.recommendations.urls")),
    path("api/v1/", include("apps.schedules.urls")),
    path("api/v1/", include("apps.assistance.urls")),
    path("api/v1/", include("apps.education.urls")),
    path("api/v1/", include("apps.notifications.urls")),
    path("api/v1/sync/", include("apps.sync.urls")),
    path("api/v1/admin/", include("apps.audit.urls")),
]
