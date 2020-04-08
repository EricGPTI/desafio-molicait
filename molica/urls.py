from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('troco/<valores>', views.troco, name='troco'),
]
