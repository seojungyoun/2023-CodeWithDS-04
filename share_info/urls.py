from django.urls import path

from . import views

app_name = 'share_info'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:info_id>/', views.detail, name='detail'),
    # path('write/', views.write, name='write'),
    path('write/write_info', views.write_info, name='write_info'),
    # path('<int:pk>/editinfo', views.editinfo, name='editinfo'),
    path('edit/<int:info_id>/', views.edit_info, name='edit_info'),
]