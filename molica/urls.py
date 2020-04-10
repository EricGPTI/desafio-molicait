from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/pagamentos', views.pagamentos, name='pagamentos'),
    path('api/v1/pagamento/', views.update_pagamento, name='update')
]
