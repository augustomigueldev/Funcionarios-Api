from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from funcionarios import views as auth_views
from funcionarios.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('funcionarios/', include('funcionarios.urls')),
    path('login', auth_views.login_view, name='login'),
    path('logout', auth_views.logout_view, name='logout'),
    path('', RedirectView.as_view(url='/funcionarios/listar')),
]
