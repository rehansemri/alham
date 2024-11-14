
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from web  import urls
from django.conf import settings

urlpatterns = [
    path("",include("web.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)