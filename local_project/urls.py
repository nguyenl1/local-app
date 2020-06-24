from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("local_app.urls", namespace = "local_app")),
    path('accounts/', include("accounts.urls")),
    path('neighborhoods/', include("neighborhoods.urls")),
]
