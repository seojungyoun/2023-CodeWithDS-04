from django.urls import path
from gradpage import views

urlpatterns = [
    path('',views.main, name="main"),
    path('computer/',views.computer, name="computer"),
    path('createArchiving/', views.create_archiving, name='create_archiving'),
    path('computer/itmedia/', views.itmedia_department, name='itmedia_department'),
    path('computer/software/', views.software_department, name='software_department'),
    path('computer/cyber/', views.cyber_department, name='cyber_department'),

]