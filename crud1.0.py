from funcoes_usuarios import *

def main():
    opcao = 0
    while opcao != -1:
        print('** CRUD **')
        print('1 - Cadastrar Usuário''\n''2 - Consultar Usuário''\n''3 - Editar Usuário''\n''4 - Apagar Usuário''\n''-1 - Encerrar')
        opcao = int(input('Opção desejada: '))
        if opcao == 1:
            cadastrar_usu()
        elif opcao == 2:
            cosultar_usu()
        elif opcao == 3:
            editar_usu()
        elif opcao == 4:
            apagar_usu()
        elif opcao == -1:
            print('Programa finalizado com sucesso!')


# Programa principal
if name == 'main':
    main()
all_data = []


def add():
    noms = input("Type in your nom: ")
    nome_usu = input("Type in your nomes_usu: ")
    email = input("Type in your email: ")
    senha = input("Type in your senhas: ")
    curso = input("Type in your curso: ")
    telefone = input("Type in your telefone: ")
    all_data.append(
        {
            "noms": noms,
            "nome_asu": nome_usu,
            "email": email,
            "curso": curso,
            "telefone": telefone,
            "senha": senha,
        }
    )