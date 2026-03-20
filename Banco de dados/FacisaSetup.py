from tabulate import tabulate

biblioteca_filme = {
    "filmes": [],
}

biblioteca_jogos = {
    "jogos": [],
}

aluguel_filme = {
    "filmes": [],
}

aluguel_jogos = {
    "jogos": [],
}


def remover_item():
    while True:
        desejo = input("Deseja remover:\n[Filme]\n[Jogo]\n")
        if 'jogo' in desejo.lower():
            nome = input("Digite o nome do jogo que você deseja remover: ").strip().title()
            if nome in biblioteca_jogos['jogos']:
                biblioteca_jogos['jogos'].remove(nome)
                print(f'{nome} removido dos jogos!')
                break
            else:
                print('Item não encontrado')
                tentar_novamente = input("Deseja continuar? [S/N] ")
                if tentar_novamente.lower() == 'n':
                    break
        elif 'filme' in desejo.lower():
            nome = input("Digite o nome do filme que você deseja remover: ").strip().title()
            if nome in biblioteca_filme['filmes']:
                biblioteca_filme['filmes'].remove(nome)
                print(f"{nome} removido dos filmes!")
                break
            else:
                print('Item não encontrado')
                tentar_novamente = input("Deseja continuar? [S/N] ")
                if tentar_novamente.lower() == 'n':
                    break


def devolver_itens():
    print(f"A lista de Filmes alugados\n{aluguel_filme['filmes']}")
    print(f"A lista de Jogos alugados\n{aluguel_jogos['jogos']}")
    desejo = input("[1]Filme\n[2]Jogo\n[3]Sair\n")
    if desejo == "1":
        nome_do_filme = input("Digite o nome do filme: ").strip().title()
        match = next((f for f in aluguel_filme['filmes'] if f.lower() == nome_do_filme.lower()), None)
        if match:
            aluguel_filme['filmes'].remove(match)
            print(f"{match} removido dos filmes alugados!")
        else:
            print("Filme não encontrado na biblioteca")

    elif desejo == "2":
        nome_do_jogo = input("Digite o nome do jogo: ").strip().title()
        match_jogo = next((j for j in aluguel_jogos['jogos'] if j.lower() == nome_do_jogo.lower()), None)
        if match_jogo:
            aluguel_jogos['jogos'].remove(match_jogo)
            print(f"{match_jogo} removido dos jogos alugados!")
        else:
            print("Jogo não encontrado na biblioteca")

    elif desejo == "3":
        return


while True:
    apelido = input('Digite seu nome: ').strip().title()
    if len(apelido) < 2:
        print('Nome inválido')
    elif not apelido.isalpha():
        print('Nome invalido')
    else:
        break

while True:
    cpf = input("Digite seu CPF: ").strip()
    if len(cpf) == 11 and cpf.isnumeric():
        break
    else:
        print("CPF invalido!")

while True:
    telefone = input("Digite seu telefone: ").strip()
    if len(telefone) == 11 and telefone.isnumeric():
        break
    else:
        print("Telefone inválido!")


def menu_geral():
    while True:
        print("=-" * 25)
        print("---LOCADORA---\n1-Cadastrar item:\n2-Listar itens:\n3-Alugar item:\n4-Devolver item:\n5-Excluir item:\n6-Sair:")
        print("=-" * 25)
        try:
            escolha = int(input("Qual a sua escolha? "))
        except ValueError:
            print("Escolha um valor válido!")
            continue

        if escolha == 1:
            while True:
                print("Menu:\n1-filme\n2-jogo\n3-Sair")
                try:
                    opcao = int(input("Escolha a sua biblioteca, Filmes ou Jogos: "))
                except ValueError:
                    print("Escolha invalida!")
                    continue

                if opcao == 1:
                    filme = input("Digite o nome do filme: ").strip().title()
                    biblioteca_filme['filmes'].append(filme)
                    print(f"Filme '{filme}' cadastrado com sucesso!")

                elif opcao == 2:
                    jogo = input("Digite o nome do jogo: ").strip().title()
                    biblioteca_jogos['jogos'].append(jogo)
                    print(f"Jogo '{jogo}' cadastrado com sucesso!")

                elif opcao == 3:
                    break

        elif escolha == 2:
            if not biblioteca_filme['filmes'] and not biblioteca_jogos['jogos']:
                print("Nenhum item cadastrado!")
                continue

            maior = max(len(biblioteca_filme['filmes']), len(biblioteca_jogos['jogos']))
            tabela = []
            for i in range(maior):
                filme = biblioteca_filme['filmes'][i] if i < len(biblioteca_filme['filmes']) else ''
                jogo = biblioteca_jogos['jogos'][i] if i < len(biblioteca_jogos['jogos']) else ''
                status_filme = 'Alugado' if filme in aluguel_filme['filmes'] else 'Disponível'
                status_jogo = 'Alugado' if jogo in aluguel_jogos['jogos'] else 'Disponível'
                tabela.append([filme, status_filme, jogo, status_jogo])

            print(tabulate(tabela, headers=['Filme', 'Status', 'Jogo', 'Status'], tablefmt='grid'))

        elif escolha == 3:
            filme_ou_jogo = input("Deseja alugar um:\n[Filme]\n[Jogo]\n").lower().strip()
            if 'filme' in filme_ou_jogo:
                nome_filme = input("Qual é o nome do filme que deseja alugar? ").strip().title()
                if nome_filme not in biblioteca_filme['filmes']:
                    print("Filme não encontrado na biblioteca!")
                elif nome_filme in aluguel_filme['filmes']:
                    print("Este filme já está alugado!")
                else:
                    aluguel_filme['filmes'].append(nome_filme)
                    print("Filme alugado com sucesso!")

            elif 'jogo' in filme_ou_jogo:
                nome_jogo = input("Qual jogo você deseja alugar? ").strip().title()
                if nome_jogo not in biblioteca_jogos['jogos']:
                    print("Jogo não encontrado na biblioteca!")
                elif nome_jogo in aluguel_jogos['jogos']:
                    print("Este jogo já está alugado!")
                else:
                    aluguel_jogos['jogos'].append(nome_jogo)
                    print("Jogo alugado com sucesso!")

        elif escolha == 4:
            devolver_itens()

        elif escolha == 5:
            remover_item()

        elif escolha == 6:
            print("Volte sempre!")
            break


menu_geral()