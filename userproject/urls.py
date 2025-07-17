from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # noqa

# ✅ Admin Panel Customization
admin.site.site_header = "Venus Attendance System Admin"
admin.site.site_title = "Venus Admin Portal"
admin.site.index_title = "Welcome to Venus Attendance System Admin Portal"

# ✅ Main URL Patterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),  # ✅ Includes all home-related routes
]

# ✅ Media Files in Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
