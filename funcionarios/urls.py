from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.listarFuncionarios),
    path('cargos', views.listarCargos),
    path('cadastro', views.cadastroFuncionario),
    path('cadastroCargo', views.cadastroCargo),
    path('excluir/<int:id>', views.excluirFuncionario),
    path('editar/<int:id>', views.editarFuncionario),
]
