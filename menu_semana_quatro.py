# Aluno: Cauã Felipe Moraes dos Santos
# Curso: Análise e Desenvolvimento de Sistemas

# Vou utilizar de funções e talvez mais algumas coisas que ainda não foram ensinadas formalmente.
# O propósito dessa semana(4) é que seja possivel utilizar as funçoes de incluir e listar estudantes em listas

# Função simples para titulos
def titulo(texto):
    space = 40
    lado = int((space - len(texto)) / 4)
    separador = '><' * lado
    print('\n' + separador + " " + texto + " " + separador + '\n' )

# Função simples para deixar uma palavra no plural
def plural(palavra):
    if palavra.endswith('r'):
        return palavra + 'es'
    else:
        return palavra + 's'

# Função para encerramento
def encerrar_menu():    
    print('Encerrando...')
    exit

# Função para adicionar items a lista
def incluir(nome_do_menu, lista):
    titulo('Menu de Inclusão')
    inclusao = input(f'Digite o(a) {nome_do_menu} a ser adicionado: ')

    if inclusao.strip():
        lista.append(inclusao.strip())
        print(f'\nO(a) {nome_do_menu} foi adicionado com sucesso.\n')
        input('Pressione [ENTER] para voltar.')

    else:
        print('Nada digitado, nenhum nome adicionado.')

# Função para mudar um item da lista
def atualizar(nome_do_menu, lista):
    titulo('Menu de Atualização.')

    if len(lista) == 0:
        print('Nenhum cadastro encontrado.')
        input('\nPressione [ENTER] para voltar.')

    else:
        print(f'\nPara continuar digite o numero do {nome_do_menu} que deseja atualizar.')
        atualizacao = input('\nNumero do item: ')
        try:    
            index = int(atualizacao) - 1
            if len(lista) > index and index >= 0:
                print(f'você deseja atualizar {lista[index]}, correto?\n')
                print('[1] Sim')
                print('[2] Não')
                print('[0] Sair')
                resposta = input('\nResposta: ')

                if resposta == '1':
                    novo = input(f'Digite a atualização: ')
                    print(f'{lista[index]} foi atualizado para {novo}.')
                    lista[index] = novo.strip()
                    input('\nPressione [ENTER] para voltar.')

                elif resposta == '2':
                    print('Voltando ao menu de atualização.')
                    atualizar(nome_do_menu, lista)

                elif resposta == '0':
                    input('\nPressione [ENTER] para voltar.')

                else:
                    print('\nO valor digitado é inválido, tente novamente.')
                    print('Voltando ao menu de atualização.')
                    atualizar(nome_do_menu, lista)
            
            else:
                print('\nNão há nenhum nome cadastrado com esse numero, verifique novamente o numero desejado em listar.')
                sair = input('\nPara sair digite 0, para tentar novamente aperte [Enter].\n Resposta: ')
                if sair == '0':
                    print('\nSaindo...')
                else:
                    excluir(nome_do_menu, lista)

        except(TypeError, ValueError):
            print('Valor invalido, tente novamente.')
            excluir(nome_do_menu, lista)

# Função para listar os items
def listar(nome_do_menu, lista):
    titulo('Menu de Listas')
    print(f'Listando {plural(nome_do_menu)}...\n')
    numero = 0
    
    if len(lista) == 0:
        print(f'Não há nenhum cadastro em {plural(nome_do_menu)}')
    
    else:
        for i in lista:
            numero += 1
            print(f'[{numero}] {i}')
    
    input('\nPressione [ENTER] para voltar.')

# Função para exclusão de itens na lista
def excluir(nome_do_menu, lista):
    titulo('Menu de Exclusão')

    if len(lista) == 0:
        print('Nenhum cadastro encontrado.')
        input('\nPressione [ENTER] para voltar.')

    else:
        print(f'\nPara continuar digite o numero do {nome_do_menu} que voce deseja excluir.')
        exclusao = input('\nNúmero do item: ')
        try:
            index = int(exclusao) - 1
            if len(lista) > index and index >= 0:
                print(f'você deseja remover {lista[index]}, correto?\n')
                print('[1] Sim')
                print('[2] Não')
                print('[0] Sair')
                resposta = input('\nResposta: ')

                if resposta == '1':
                    print(f'Removendo {lista[index]}...')
                    lista.remove(lista[index])
                    input('\nPressione [ENTER] para voltar.')

                elif resposta == '2':
                    print('Voltando ao menu de exclusão.')
                    excluir(nome_do_menu, lista)

                elif resposta == '0':
                    input('\nPressione [ENTER] para voltar.')

                else:
                    print('\nO valor digitado é inválido, tente novamente.')
                    print('Voltando ao menu de exclusão.')
                    excluir(nome_do_menu, lista)
            
            else:
                print('\nNão há nenhum nome cadastrado com esse numero, verifique novamente o numero desejado em listar.')
                sair = input('\nPara sair digite 0, para tentar novamente aperte [Enter].\n Resposta: ')
                if sair == '0':
                    print('\nSaindo...')

                else:
                    excluir(nome_do_menu, lista)

        except(TypeError, ValueError):
            print('Valor invalido, tente novamente.')
            excluir(nome_do_menu, lista)

# Criando uma função para o menu pricipal
def menu_principal():

    # Mostrando o menu principal
    titulo('Menu Principal')
    
    print('[1] Gerenciar estudantes')
    print('[2] Gerenciar disciplinas')
    print('[3] Gerenciar professores')
    print('[4] Gerenciar turmas')
    print('[5] Gerenciar matrículas')
    print('[0] Sair')

    # Coletando a opção de menu secundario
    opcao_de_menu = (input('\nInforme a opção desejada: '))

    # Dicionario que puxa o menu correspondente a opção selecionada
    try:    
        opcoes = {
            '1' : menu_estudantes,
            '2' : menu_disciplinas,
            '3' : menu_professores,
            '4' : menu_turmas,
            '5' : menu_matriculas,
            '0' : encerrar_menu
            }
        opcao_de_menu = opcoes.get(opcao_de_menu)
        opcao_de_menu()
    except:
        print('\nO valor digitado é inválido, tente novamente.')
        menu_principal()

# Função base para criação de cada menu secundario
def menu_secundario(nome, lista):

    # Mostrando o menu secundario
    titulo(f'Menu de {(nome)}')

    print(f'[1] Incluir {nome.lower()}')
    print(f'[2] Atualizar {nome.lower()}')
    print(f'[3] Listar {plural(nome.lower())}')
    print(f'[4] Excluir {nome.lower()}')
    print(f'[0] Voltar ao menu principal')

    # Coletando a opção de acão
    opcao_sub_menu = (input('\nInforme a opção desejada: '))
    try:
        opcoes_secundarias = {
            '1' : incluir,
            '2' : atualizar,
            '3' : listar,
            '4' : excluir,
            }
        if opcao_sub_menu == '0':
            menu_principal()
        else:
            opcao_sub_menu = opcoes_secundarias.get(opcao_sub_menu)
            opcao_sub_menu(nome.lower(), lista)
            
    except:
        print('\nO valor digitado é inválido, tente novamente.')
    menu_secundario(nome, lista)

# Menu de Estudantes
def menu_estudantes():
    estudantes = []
    menu_secundario('Estudante', estudantes)

# Menu de Disciplinas
def menu_disciplinas():
    disciplinas = []
    menu_secundario('Disciplina', disciplinas)

# Menu de Professores
def menu_professores():
    professores = []
    menu_secundario('Professor', professores)

# Menu de Turmas
def menu_turmas():
    turmas = []
    menu_secundario('Turmas', turmas)

# Menu de Matriculas
def menu_matriculas():
    matriculas = []
    menu_secundario('Matriculas', matriculas)

menu_principal()
