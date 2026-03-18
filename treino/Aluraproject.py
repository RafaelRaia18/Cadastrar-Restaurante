import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa', 'ativo':False},
                {'nome':'Pízza Suprema', 'categoria':'pizza', 'ativo':True},
                {'nome':'Coxinha', 'categoria':'Italiano', 'ativo':False}]


def exibirNomeDoPrograma():
    print('SABOR EXPRESS')


def limparAtela():
    os.system('cls')


def exibirOpcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. sair')


def voltarAomenuPrincipal():
    input('\nDigite uma tecla para sair')

def opcaoInvalida():
    print('Opcão Invalida')
    voltarAomenuPrincipal()

def exibirSubtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrarNovoRestaurante():

    exibirSubtitulo('cadastro de novos restaurantes')
    nomeDoRestaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nomeDoRestaurante}: ')
    dadosDoRestaurante = {'nome': nomeDoRestaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dadosDoRestaurante)
    print(f'\nO restaurante {nomeDoRestaurante} foi cadastrado com sucesso!')
    voltarAomenuPrincipal()

def listarRestaurantes():
    exibirSubtitulo('listando restaurantes')
    for restaurante in restaurantes:
        nomeRestaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'desativado'
        print(f'. {nomeRestaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')
    voltarAomenuPrincipal()

def ativarRestaurante():
    exibirSubtitulo('Alternando estado do restaurante')
    nomeRestaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restauranteEncontrado = False
    for restaurante in restaurantes:
        if nomeRestaurante == restaurante['nome']:
            restauranteEncontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nomeRestaurante} foi alterado com sucesso!' if restaurante ['ativo'] else f'O restaurante {nomeRestaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restauranteEncontrado:
        print('O restaurante não foi encontrado')

    voltarAomenuPrincipal()

def escolherOpcao():
    return int(input('Escolha uma opcao:'))


while True:
    limparAtela()
    exibirOpcoes()

    opcao = escolherOpcao()

    if opcao == 1:
        cadastrarNovoRestaurante()
    elif opcao == 2:
        listarRestaurantes()
    elif opcao == 3:
        ativarRestaurante()
    elif opcao == 4:
        print('saindo')
        break
    else:
        opcaoInvalida()
        continue
