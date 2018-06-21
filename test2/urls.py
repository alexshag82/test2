from django.urls import path
from firstapp import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('list/<int:id>/', views.list),
    path('gm_ipadr/', views.gm_ipadr),
    path('gm_ipadr/<int:id>/', views.gm_ipadr),
    path('edit/<int:id>/', views.edit),
    path('edit_gm_ipadr/<int:id>/', views.edit_gm_ipadr),
    path('delete/<int:id>/', views.delete),
]
