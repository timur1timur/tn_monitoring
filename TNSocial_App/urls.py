from django.contrib import admin
from django.urls import path, include
from .views import redirect_url

urlpatterns = [
    path('', redirect_url),
    path('admin/', admin.site.urls),
    path('msn_tn/', include('monitoring.urls')),

]