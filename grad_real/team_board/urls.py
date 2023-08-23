from django.urls import path

from . import views

app_name = 'team_board'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('write/write_team_board', views.write_team_board, name='write_board'),
    path('<int:board_id>/create_reply', views.create_reply, name='create_reply'),
    path('<int:pk>/editboard', views.editboard, name='editboard'),

]