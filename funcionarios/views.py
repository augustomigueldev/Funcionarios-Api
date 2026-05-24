from django.shortcuts import render
from .models import Funcionario, Cargo
from datetime import datetime
from django.http import HttpResponseRedirect


def listarFuncionarios(request):
    if request.method == "GET" and request.GET.get('busca'):
        funcionarios = Funcionario.objects.filter(nome__icontains=request.GET.get('busca'))
    else:
        funcionarios = Funcionario.objects.all()

    return render(request, "listarFuncionarios.html", {"funcionarios": funcionarios})


def listarCargos(request):
    cargos = Cargo.objects.all()
    return render(request, "listarCargos.html", {"cargos": cargos})


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

        return HttpResponseRedirect('/funcionarios/listar')

    cargos = Cargo.objects.all()
    return render(request, "cadastroFuncionario.html", {'cargos': cargos})


def cadastroCargo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        novo_cargo = Cargo(nome=nome)
        novo_cargo.save()
        return HttpResponseRedirect('/funcionarios/cargos')

    return render(request, "cadastroCargo.html")


def excluirFuncionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    funcionario.delete()
    return HttpResponseRedirect('/funcionarios/listar')


def editarFuncionario(request, id):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_admissao = request.POST.get('data_admissao')
        salario = request.POST.get('salario')
        cargo = Cargo.objects.get(id=request.POST.get('cargo'))

        func = Funcionario.objects.get(id=id)
        func.nome = nome
        func.cpf = cpf
        func.email = email
        func.telefone = telefone
        func.data_admissao = data_admissao
        func.salario = salario
        func.cargo = cargo
        func.save()

        return HttpResponseRedirect('/funcionarios/listar')
    else:
        funcionario = Funcionario.objects.get(id=id)
        cargos = Cargo.objects.all()

    return render(request, "editarFuncionario.html", {'funcionario': funcionario, 'cargos': cargos})
