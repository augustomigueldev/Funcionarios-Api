from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.db import IntegrityError
from django.contrib import messages
from .models import Funcionario, Cargo
from rest_framework import viewsets
from .serializers import FuncionarioSerializer, CargoSerializer


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/funcionarios/listar')

    erro = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/funcionarios/listar')
        else:
            erro = 'Usuário ou senha incorretos.'

    return render(request, 'login.html', {'erro': erro})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required
def listarFuncionarios(request):
    if request.method == "GET" and request.GET.get('busca'):
        funcionarios = Funcionario.objects.filter(nome__icontains=request.GET.get('busca'))
    else:
        funcionarios = Funcionario.objects.all()

    return render(request, "listarFuncionarios.html", {"funcionarios": funcionarios})


@login_required
def listarCargos(request):
    cargos = Cargo.objects.all()
    return render(request, "listarCargos.html", {"cargos": cargos})


@permission_required('funcionarios.add_funcionario', login_url='/funcionarios/listar')
def cadastroFuncionario(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_admissao = request.POST.get('data_admissao')
        salario = request.POST.get('salario')
        cargo_id = request.POST.get('cargo')
        cargo = Cargo.objects.get(id=cargo_id)

        try:
            novo_funcionario = Funcionario(
                nome=nome,
                cpf=cpf,
                email=email,
                telefone=telefone,
                data_admissao=data_admissao,
                salario=salario,
                cargo=cargo
            )
            novo_funcionario.save()
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return HttpResponseRedirect('/funcionarios/listar')
        except IntegrityError:
            messages.error(request, 'Já existe um funcionário cadastrado com este CPF, E-mail ou Telefone.')
            cargos = Cargo.objects.all()
            return render(request, "cadastroFuncionario.html", {'cargos': cargos})

    cargos = Cargo.objects.all()
    return render(request, "cadastroFuncionario.html", {'cargos': cargos})


@permission_required('funcionarios.add_cargo', login_url='/funcionarios/listar')
def cadastroCargo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        novo_cargo = Cargo(nome=nome)
        novo_cargo.save()
        return HttpResponseRedirect('/funcionarios/cargos')

    return render(request, "cadastroCargo.html")


@permission_required('funcionarios.delete_funcionario', login_url='/funcionarios/listar')
def excluirFuncionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    funcionario.delete()
    return HttpResponseRedirect('/funcionarios/listar')


@permission_required('funcionarios.change_cargo', login_url='/funcionarios/cargos')
def editarCargo(request, id):
    cargo = Cargo.objects.get(id=id)
    if request.method == "POST":
        cargo.nome = request.POST.get('nome')
        cargo.save()
        return HttpResponseRedirect('/funcionarios/cargos')
    return render(request, "editarCargo.html", {'cargo': cargo})


@permission_required('funcionarios.change_funcionario', login_url='/funcionarios/listar')
def editarFuncionario(request, id):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_admissao = request.POST.get('data_admissao')
        salario = request.POST.get('salario')
        cargo = Cargo.objects.get(id=request.POST.get('cargo'))

        try:
            func = Funcionario.objects.get(id=id)
            func.nome = nome
            func.cpf = cpf
            func.email = email
            func.telefone = telefone
            func.data_admissao = data_admissao
            func.salario = salario
            func.cargo = cargo
            func.save()
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return HttpResponseRedirect('/funcionarios/listar')
        except IntegrityError:
            messages.error(request, 'Já existe outro funcionário cadastrado com este CPF, E-mail ou Telefone.')
            funcionario = Funcionario.objects.get(id=id)
            cargos = Cargo.objects.all()
            return render(request, "editarFuncionario.html", {'funcionario': funcionario, 'cargos': cargos})
    else:
        funcionario = Funcionario.objects.get(id=id)
        cargos = Cargo.objects.all()

    return render(request, "editarFuncionario.html", {'funcionario': funcionario, 'cargos': cargos})


@permission_required('funcionarios.delete_cargo', login_url='/funcionarios/cargos')
def excluirCargo(request, id):
    cargo = Cargo.objects.get(id=id)
    cargo.delete()
    return HttpResponseRedirect('/funcionarios/cargos')


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
