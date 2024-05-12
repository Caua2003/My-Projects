def titulo(texto):  # Função para formatação de titulos, sem precisar fazer manualmente toda vez em um menu novo
    space = 40
    lado = int((space - len(texto)) / 2)
    separador = '=' * lado
    print(separador + " " + texto + " " + separador)


def plural(palavra):         # Testando pra ver se fica mais facil na formatção
    if palavra.endswith('r'):
        return palavra + 'es'
    else:
        return palavra + 's'


def menu(menu_nome, opcoes):    # base para o menu pricipal, talvez colocar junto com o menu principal?
    titulo(menu_nome)           # ou talvez não, foi usado pro menu secundario tambem
    print()
    for key, item in opcoes.items():
        print(f'[{key}] {item}.')


def menu_principal():       # Cada opção puxa um menu diferente
    prin_opcoes = {'1': 'Gerenciar Estudantes',
                   '2': 'Gerenciar Disciplinas',
                   '3': 'Gerenciar Professores',
                   '4': 'Gerenciar Turmas',
                   '5': 'Gerenciar Matriculas',
                   '9': 'Sair'
                   }
    menu('Menu principal', prin_opcoes)
    escolha = int(input('\nDigite sua Escolha: '))
    if escolha == 1:
        menu_estudantes()

    elif escolha == 2:
        menu_disciplinas()

    elif escolha == 3:
        menu_professores()

    elif escolha == 4:
        menu_turmas()

    elif escolha == 5:
        menu_matriculas()

    elif escolha == 9:
        exit(0)

    else:
        print('\nErro, digite um valor valido.\n')
        menu_principal()


def menu_secundario(nome_menu):     # Criação de uma função base para os sub menus
    sec_opcoes = {'1': f'Incluir {nome_menu}',
                  '2': f'Listar {plural(nome_menu)}',
                  '3': f'Atualizar {nome_menu}',
                  '4': f'Excluir {nome_menu}',
                  '9': 'Voltar ao menu principal'
                  }
    menu('Menu de ' + plural(nome_menu), sec_opcoes)


def menu_estudantes():
    menu_secundario('Estudante')
    escolha = int(input('\nDigite sua Escolha: '))
    if escolha == 1:
        print('Incluindo...')   # Parte sem desenvolvimento
    elif escolha == 2:                                              # Esse código se repete muito,
        print('Listando...')    # Parte sem desenvolvimento         # talvez usar uma função para redução de códigos
    elif escolha == 3:
        print('Atualizando...')    # Parte sem desenvolvimento
    elif escolha == 4:
        print('Excluindo...')   # Parte sem desenvolvimento
    elif escolha == 9:
        menu_principal()
    else:
        print('\nErro, digite um valor valido\n')
        menu_estudantes()


def menu_disciplinas():
    menu_secundario('Disciplina')
    escolha = int(input('\nDigite sua Escolha: '))
    if escolha == 1:
        print('Incluindo...')   # Parte sem desenvolvimento
    elif escolha == 2:
        print('Listando...')    # Parte sem desenvolvimento
    elif escolha == 3:
        print('Atualizando...')    # Parte sem desenvolvimento
    elif escolha == 4:
        print('Excluindo...')   # Parte sem desenvolvimento
    elif escolha == 9:
        menu_principal()
    else:
        print('\nErro, digite um valor valido\n')
        menu_disciplinas()


def menu_professores():
    menu_secundario('Professor')
    escolha = int(input('\nDigite sua Escolha: '))
    if escolha == 1:
        print('Incluindo...')   # Parte sem desenvolvimento
    elif escolha == 2:
        print('Listando...')    # Parte sem desenvolvimento
    elif escolha == 3:
        print('Atualizando...')    # Parte sem desenvolvimento
    elif escolha == 4:
        print('Excluindo...')   # Parte sem desenvolvimento
    elif escolha == 9:
        menu_principal()
    else:
        print('\nErro, digite um valor valido\n')
        menu_professores()


def menu_turmas():
    menu_secundario('Turma')
    escolha = int(input('\nDigite sua Escolha: '))
    if escolha == 1:
        print('Incluindo...')   # Parte sem desenvolvimento
    elif escolha == 2:
        print('Listando...')    # Parte sem desenvolvimento
    elif escolha == 3:
        print('Atualizando...')    # Parte sem desenvolvimento
    elif escolha == 4:
        print('Excluindo...')   # Parte sem desenvolvimento
    elif escolha == 9:
        menu_principal()
    else:
        print('\nErro, digite um valor valido\n')
        menu_turmas()


def menu_matriculas():
    menu_secundario('Matricula')
    escolha = int(input('\nDigite sua Escolha: '))
    if escolha == 1:
        print('Incluindo...')   # Parte sem desenvolvimento
    elif escolha == 2:
        print('Listando...')    # Parte sem desenvolvimento
    elif escolha == 3:
        print('Atualizando...')    # Parte sem desenvolvimento
    elif escolha == 4:
        print('Excluindo...')   # Parte sem desenvolvimento
    elif escolha == 9:
        menu_principal()
    else:
        print('\nErro, digite um valor valido\n')
        menu_matriculas()


menu_principal()
