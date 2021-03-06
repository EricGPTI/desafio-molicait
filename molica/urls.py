from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagamentos, name='pagamentos'),
    path('api/v1/pagamentos', views.pagamentos, name='pagamentos'),
    path('api/v1/pagamento/update/', views.update_pagamento, name='update'),
    path('api/v1/pagamento/delete/<str:id_pagamento>', views.delete_pagamento, name='delete'),
]
