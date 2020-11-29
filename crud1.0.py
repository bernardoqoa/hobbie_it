from funcoes_crud import *


def main():
    opcoes = [1, 2, 3, 4, -1]
    opcao = 0
    while opcao != -1:
        print('** CRUD **')
        print('1 - Cadastrar Usuário\n2 - Consultar Usuário\n3 - Editar Usuário\n4 - Apagar Usuário\n-1 - Encerrar')
        opcao = int(input('Opção desejada: '))
        while opcao not in opcoes:
            print("Você digitou uma opção invalida.")
            opcao = int(input("Digite a opção desejada: "))
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
if __name__ == '__main__':
    main()
