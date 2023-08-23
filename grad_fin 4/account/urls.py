from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('my_page/', views.my_page, name='my_page'),
    path('my_page/update/', views.update, name="my_page_update"),
    path('my_page/change_password/', views.change_password, name="re_password")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)