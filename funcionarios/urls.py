from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cargos', views.CargoViewSet)
router.register(r'funcionarios', views.FuncionarioViewSet)

urlpatterns = [
    path('listar', views.listarFuncionarios),
    path('cargos', views.listarCargos),
    path('cadastro', views.cadastroFuncionario),
    path('cadastroCargo', views.cadastroCargo),
    path('excluir/<int:id>', views.excluirFuncionario),
    path('excluirCargo/<int:id>', views.excluirCargo),
    path('editarCargo/<int:id>', views.editarCargo),
    path('editar/<int:id>', views.editarFuncionario),
]
