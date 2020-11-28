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


#def editar_usu():



#def apagar_usu():
