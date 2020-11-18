nomes = []
nomes_usu = []
emails = []
senhas = []
cursos = []
telefones = []
interesses_geral = []
interesses = ["JOGOS", "FILMES", "FUTEBOL", "MÚSICA"]
opcoes = [1, 2, 3, 4, -1]
opcao = 0
i = 0

print('****** CRUD ******')
print('1 - Cadastrar Usuário')
print('2 - Consultar Usuário')
print('3 - Editar Usuário')
print('4 - Apagar Usuário')
print('-1 - Encerrar')

while opcao != -1:

    opcao = int(input("Digite a opção desejada: "))
    while opcao not in opcoes:
        print("Você digitou uma opção invalida.")
        opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o seu nome e sobrenome: ")
        nomes.append(nome)
        nome_usu = input("Digite o nome do seu usuário: ")
        nomes_usu.append(nome_usu)
        email = input("Digite o seu email: ")
        emails.append(email)
        curso = input("Qual o seu curso? ")
        cursos.append(curso)
        telefone = input('Digite seu telefone: ')
        telefones.append(telefone)
        senha = input('Digite sua senha: ')
        senha2 = str(input('Digite novamente sua senha: '))
        while senha2 != senha:
            senha2 = str(input('Você digitou errado. Digite novamente sua senha: '))
        senhas.append(senha)
        print(interesses)
        i = int(input('Quantos desses interesses você se interessa? '))
        interesses_usu = []
        for c in range(i):
            interesse_usu = input('Digite um desses interesses: ').upper()
            while interesse_usu not in interesses:
                print('Você digitou um interesse indisponivel!')
                print(f'Os interesses disponiveis são: {interesses}')
                interesse_usu = input('Digite novamente: ').upper()
            interesses_usu.append(interesse_usu)
        interesses_geral.append(interesses_usu)

    if opcao == 2:

        y = input('Digite seu nome de usuário: ')
        while y not in nomes_usu:
            y = input("Você digitou um nome de usuário inválido. Digite novamente: ")
        x = nomes_usu.index(y)
        print(f'O seu nome de perfil é: {nomes[x]}')
        print(f'O seu nome de usuário é: {nomes_usu[x]}')
        print(f'O seu curso é: {cursos[x]}')
        print(f'Os seus interesses são: {interesses_geral[x]}')
        print(f'O seu email é: {emails[x]}')
        print(f'O seu telefone é: {telefones[x]}')
        p = ''
        while p != 'p':
            p = str(input('Digite "p" para prosseguir ou "c" para consultar outro usuário: '))
            while p != 'p' and p != 'c':
                p = str(input('Opção invalida! Digite "p" para prosseguir ou "c" para consultar outro usuário: '))
            while p == 'c':
                y = input('Digite seu nome de usuário: ')
                while y not in nomes_usu:
                    y = input("Você digitou um nome de usuário inválido. Digite novamente: ")
                x = nomes_usu.index(y)
                print(f'O seu nome de perfil é: {nomes[x]}')
                print(f'O seu nome de usuário é: {nomes_usu[x]}')
                print(f'O seu curso é: {cursos[x]}')
                print(f'Os seus interesses são: {interesses_geral[x]}')
                print(f'O seu email é: {emails[x]}')
                print(f'O seu telefone é: {telefones[x]}')
                p = ''

    if opcao == 3:

        y = input('Digite o nome de usuário do perfil que você deseja editar: ')
        while y not in nomes_usu:
            y = input("Você digitou um nome de usuário inválido. Digite novamente: ")
        x = nomes_usu.index(y)
        print('Opções:')
        print('Digite 1 para editar o nome')
        print('Digite 2 para editar o nome de usuário')
        print('Digite 3 para editar o email')
        print('Digite 4 para editar o telefone')
        print('Digite 5 para editar o curso')
        print('Digite 6 para editar os interesses')
        print('Digite 7 para editar a senha')
        editar = int(input('Digite -1 para voltar ao CRUD: '))
        if editar == 1:
            nomes[x] = input("Digite seu novo nome: ")
        if editar == 2:
            nomes_usu[x] = input("Digite seu novo nome de usuário: ")
        if editar == 3:
            emails[x] = input("Digite seu novo email: ")
        if editar == 4:
            telefones[x] = input("Digite seu novo telefone: ")
        if editar == 5:
            cursos[x] = input("Digite seu novo curso: ")
        if editar == 6:
            editar_escolha = 0
            while editar_escolha != -1:
                print(f'Seus interesses atuais são: {interesses_geral[x]}')
                print(f"Os interesses disponiveis são: {interesses}")
                print('1 - Adicionar um novo interesse')
                print('2 - Excluir um interesse: ')
                editar_escolha = int(input('-1 - Para voltar ao menu de edição: '))
                if editar_escolha == 1:
                    interesses_geral[x].append(input("Digite o novo interesse: ").upper())
                if editar_escolha == 2:
                    int_remove = (input("Digite o interesse a ser removido: ").upper())
                    while int_remove not in interesses_geral[x]:
                        int_remove = (input("Interesse invalido! Digite novamente o interesse a ser removido: ").upper())
                    if int_remove in interesses_geral[x]:
                        interesses_geral[x].remove(int_remove)
        if editar == 7:
            senha = input('Digite sua senha atual: ')
            while senha != senhas[x]:
                senha = input("Essa não é a sua senha atual. Tente novamente: ")
            if senha == senhas[x]:
                senha_nova = str(input('Digite sua nova senha: '))
                senha_conf = str(input('Confirme sua nova senha: '))
            while senha_conf != senha_nova:
                senha_conf = str(input('Você digitou errado. Digite novamente sua senha: '))
            senhas[x] = senha_conf
            voltar = input('Senha alterada com sucesso. Digite "p" para voltar ao CRUD: ').upper()
            while voltar != 'P':
                voltar = input('Você digitou errado! Digite "p" para voltar ao CRUD: ').upper()

    if opcao == 4:
        y = input('Digite o nome de usuário do perfil que você deseja excluir: ')
        while y not in nomes_usu:
            y = input("Você digitou um nome de usuário inválido. Digite novamente: ")
        x = nomes_usu.index(y)
        certeza = ''
        while certeza != 'N' and certeza != 'S':
            certeza = input(f"Você realemente deseja excluir o perfil: {nomes_usu[x]}\nS - Sim\nN - Não: ").upper()
        if certeza == 'S':
            nomes.pop(x)
            nomes_usu.pop(x)
            emails.pop(x)
            senhas.pop(x)
            cursos.pop(x)
            telefones.pop(x)
            interesses_geral.pop(x)

    print('****** CRUD ******')
    print('1 - Cadastrar Usuário')
    print('2 - Consultar Usuário')
    print('3 - Editar Usuário')
    print('4 - Apagar Usuário')
    print('-1 - Encerrar')
