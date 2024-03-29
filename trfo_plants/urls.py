from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'), name = "home"),
    path('plants/', include('plants.urls')),
    path('admin/', admin.site.urls),
    #path('create-new-user/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name="logout"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)