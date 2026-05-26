from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from funcionarios import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('funcionarios.urls')),
    path('login', auth_views.login_view, name='login'),
    path('logout', auth_views.logout_view, name='logout'),
    path('', RedirectView.as_view(url='/funcionarios/listar')),
]
