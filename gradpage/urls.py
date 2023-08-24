from django.urls import path
from gradpage import views

urlpatterns = [
    path('', views.main, name="main"),
    path('computer/', views.computer, name="computer"),
    path('createArchiving/', views.create_archiving, name='create_archiving'),
    path('computer/itmedia/', views.itmedia_department, name='itmedia_department'),
    # computer에서 dropdown으로 선택학과 - 아카이빙 (미대까지)
    path('computer/software/', views.software_department, name='software_department'),
    path('computer/cyber/', views.cyber_department, name='cyber_department'),
    path('technology/', views.technology_view, name='technology'),
    # technology에서 글씨 선택학과
    path('technology/bio_department/', views.bio_department, name='bio_department'),
    path('technology/itemedia_department/', views.itmedia_department, name='itemedia_department'),
    path('technology/cyber_department/', views.cyber_department, name='cyber_department'),
    path('technology/sports_department/', views.sports_department, name='sports_department'),
    path('technology/software_department/', views.software_department, name='software_department'),
    path('technology/food_department/', views.food_department, name='food_department'),
    path('technology/infstatic_department/', views.infstatic_department, name='infstatic_department'),
    path('technology/chemical_department/', views.chemical_department, name='chemical_department'),
    path('technology/math_department/', views.math_department, name='math_department'),
    # technology - dropdown에서 선택학과 
    path('technology/bio_department/', views.bio_department, name='bio_department'),

]
