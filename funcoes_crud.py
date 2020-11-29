interesses = ["JOGOS", "FILMES", "FUTEBOL", "MÚSICA"]

def cadastrar_usu():
    usu_info = {}
    print('1. Cadastro:')
    nome = input("Nome completo: ")
    usu_info['nome'] = nome + ','
    nome_usu = input("Nome de usuário: ") + ','
    email = input("Email: ")
    usu_info['email'] = email + ','
    senha = input("Senha: ")
    senha2 = input("Confirme sua senha:")
    while senha != senha2:
        senha2 = input('As senhas não coincidem! Digite novamente: ')
    if senha == senha2:
        usu_info['senha'] = senha + ','
    curso = input("Curso: ")
    usu_info['curso'] = curso + ','
    telefone = input("Telefone: ")
    usu_info['telefone'] = telefone + ','
    print(interesses)
    i = int(input('Quantos desses interesses você se interessa? '))
    interesses_usu = []
    for c in range(i):
        interesse_usu = input('Digite um desses interesses: ').upper()
        while interesse_usu not in interesses:
            print('Você digitou um interesse indisponivel!')
            print(f'Os interesses disponiveis são: {interesses}')
            interesse_usu = input('Digite novamente: ').upper()
        if c == (i-1):
            interesse_usu = interesse_usu + '\n'
        else:
            interesse_usu = interesse_usu + ','
        interesses_usu.append(interesse_usu)
    usu_info['interesses'] = interesses_usu
    usuarios = open('usuarios.txt', 'a', encoding='utf8')
    usuarios.writelines(nome_usu)
    for info in usu_info:
        usuarios.writelines(usu_info[info])
    usuarios.close()


def cosultar_usu():
    print('2. Consulta:')
    usuarios = open('usuarios.txt', 'r', encoding='utf8')
    lista_usuarios = usuarios.readlines()
    usu = input('Digite o nome de usuário:')
    for x in range(len(lista_usuarios)):
        usu_info = lista_usuarios[x].split(',')
        if usu == usu_info[0]:
            indice = x
    usu_info = lista_usuarios[indice].split(',')
    print(f'Nome: {usu_info[1]}')
    print(f'Nome de usuário: {usu_info[0]}')
    print(f'Email: {usu_info[2]}')
    print(f'Curso: {usu_info[4]}')
    print(f'Telefone: {usu_info[5]}')
    l = []
    for y in usu_info[6:]:
        if usu_info.index(y) != (len(usu_info)-1):
            l.append(y)
        else:
            l.append(y.replace("\n", ""))
    print(f'Interesses: {l}')


def editar_usu():
    print('3. Edição:')
    usuarios = open('usuarios.txt', 'r', encoding='utf8')
    lista_usuarios = usuarios.readlines()
    usuarios.close()
    usu = input('Digite o nome de usuário:')
    for x in range(len(lista_usuarios)):
        usu_info = lista_usuarios[x].split(',')
        if usu == usu_info[0]:
            indice = x
    usu_info = lista_usuarios[indice].split(',')
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
        usu_info[1] = input("Digite seu novo nome: ")
    if editar == 2:
        usu_info[0] = input("Digite seu novo nome de usuário: ")
    if editar == 3:
        usu_info[2] = input("Digite seu novo email: ")
    if editar == 4:
        usu_info[5] = input("Digite seu novo telefone: ")
    if editar == 5:
        usu_info[4] = input("Digite seu novo curso: ")
    if editar == 6:
        editar_escolha = 0
        l = []
        for y in usu_info[6:]:
            if usu_info.index(y) != (len(usu_info) - 1):
                l.append(y)
            else:
                l.append(y.replace("\n", ""))
        while editar_escolha != -1:
            print(f'Seus interesses atuais são: {l}')
            print(f"Os interesses disponiveis são: {interesses}")
            print('1 - Adicionar um novo interesse')
            print('2 - Excluir um interesse: ')
            editar_escolha = int(input('-1 - Para voltar ao menu de edição: '))
            if editar_escolha == 1:
                l.append(input("Digite o novo interesse: ").upper())
                z = []
                for y in l:
                    if l.index(y) != (len(l) - 1):
                        z.append(y)
                    else:
                        z.append(y.replace("\n", ""))
                z[-1] = z[-1] + '\n'
                usu_info[6:] = z
            if editar_escolha == 2:
                int_remove = (input("Digite o interesse a ser removido: ").upper())
                while int_remove not in l:
                    int_remove = (input("Interesse invalido! Digite novamente o interesse a ser removido: ").upper())
                if int_remove in l:
                    l.remove(int_remove)
                    z = []
                    for y in l:
                        z.append(y)
                    if '\n' not in z[-1]:
                        z[-1] = z[-1] + '\n'
                        usu_info[6:] = z
    if editar == 7:
        senha = input('Digite sua senha atual: ')
        while senha != usu_info[3]:
            senha = input("Essa não é a sua senha atual. Tente novamente: ")
        if senha == usu_info[3]:
            senha_nova = str(input('Digite sua nova senha: '))
            senha_conf = str(input('Confirme sua nova senha: '))
        while senha_conf != senha_nova:
            senha_conf = str(input('Você digitou errado. Digite novamente sua senha: '))
        usu_info[3] = senha_conf
        voltar = input('Senha alterada com sucesso. Digite "p" para voltar ao CRUD: ').upper()
        while voltar != 'P':
            voltar = input('Você digitou errado! Digite "p" para voltar ao CRUD: ').upper()

    lista_usuarios[indice] = ','.join(usu_info)
    usuarios = open('usuarios.txt', 'w', encoding='utf8')
    usuarios.writelines(lista_usuarios)
    usuarios.close()


def apagar_usu():
    print('4. Remoção:')
    usuarios = open('usuarios.txt', 'r', encoding='utf8')
    lista_usuarios = usuarios.readlines()
    usuarios.close()
    usu = input('Digite o nome de usuário:')
    for x in range(len(lista_usuarios)):
        usu_info = lista_usuarios[x].split(',')
        if usu == usu_info[0]:
            indice = x
    del lista_usuarios[indice]
    usuarios = open('usuarios.txt', 'w', encoding='utf8')
    usuarios.writelines(lista_usuarios)
    usuarios.close()
