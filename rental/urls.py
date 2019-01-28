from django.urls import include, path
from django.contrib import admin
from .api import router

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
]
