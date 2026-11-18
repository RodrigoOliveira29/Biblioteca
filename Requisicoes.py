from datetime import date, timedelta

# Lista de livros da biblioteca
livros = [
    {"id": 1, "titulo": "Os Lusíadas", "disponivel": True},
    {"id": 2, "titulo": "A Cidade e as Serras", "disponivel": True},
    {"id": 3, "titulo": "Mensagem", "disponivel": True},
    {"id": 4, "titulo": "Harry Potter", "disponivel": True}
]

# Lista de requisições ativas
requisicoes = []

# Histórico de requisições
historico = []


# Mostrar livros disponíveis
def mostrar_livros():
    print("\n--- LIVROS DISPONÍVEIS ---")

    for livro in livros:
        if livro["disponivel"]:
            print(livro["id"], "-", livro["titulo"])


# Requisitar um livro
def requisitar_livro():
    mostrar_livros()

    try:
        id_livro = int(input("\nIndica o ID do livro: "))
    except ValueError:
        print("ID inválido.")
        return

    for livro in livros:
        if livro["id"] == id_livro:

            if livro["disponivel"]:
                data_inicio = date.today()
                data_limite = data_inicio + timedelta(days=14)

                nova_requisicao = {
                    "titulo": livro["titulo"],
                    "data_requisicao": data_inicio,
                    "data_limite": data_limite
                }

                requisicoes.append(nova_requisicao)
                livro["disponivel"] = False

                print("\nLivro requisitado com sucesso!")
                print("Data limite de devolução:", data_limite)

            else:
                print("Este livro já está requisitado.")

            return

    print("Livro não encontrado.")


    # Consultar livros requisitados
def consultar_requisicoes():
    print("\n--- LIVROS REQUISITADOS ---")

    if len(requisicoes) == 0:
        print("Não tens livros requisitados.")
        return

    for livro in requisicoes:
        print("Livro:", livro["titulo"])
        print("Data limite:", livro["data_limite"])
        print("-------------------------")


# Consultar datas limite
def consultar_datas():
    print("\n--- DATAS DE DEVOLUÇÃO ---")

    for livro in requisicoes:
        print(livro["titulo"], "-", livro["data_limite"])


# Devolver um livro
def devolver_livro():
    consultar_requisicoes()

    if len(requisicoes) == 0:
        return

    titulo = input("\nIndica o nome do livro a devolver: ")

    for requisicao in requisicoes:
        if requisicao["titulo"].lower() == titulo.lower():

            requisicao["data_devolucao"] = date.today()
            historico.append(requisicao.copy())

            requisicoes.remove(requisicao)

            for livro in livros:
                if livro["titulo"] == titulo:
                    livro["disponivel"] = True

            print("Livro devolvido com sucesso!")
            return

    print("Não tens esse livro requisitado.")

# Consultar histórico
def consultar_historico():
    print("\n--- HISTÓRICO DE REQUISIÇÕES ---")

    if len(historico) == 0:
        print("Ainda não existem requisições anteriores.")
        return

    for livro in historico:
        print("Livro:", livro["titulo"])
        print("Requisitado em:", livro["data_requisicao"])
        print("Devolvido em:", livro["data_devolucao"])
        print("-------------------------")

# Menu principal
while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Mostrar livros disponíveis")
    print("2 - Requisitar livro")
    print("3 - Consultar livros requisitados")
    print("4 - Consultar datas de devolução")
    print("5 - Devolver livro")
    print("6 - Consultar histórico")
    print("0 - Sair")

    opcao = input("\nEscolhe uma opção: ")

    if opcao == "1":
        mostrar_livros()

    elif opcao == "2":
        requisitar_livro()

    elif opcao == "3":
        consultar_requisicoes()

    elif opcao == "4":
        consultar_datas()

    elif opcao == "5":
        devolver_livro()

    elif opcao == "6":
        consultar_historico()

    elif opcao == "0":
        print("A sair do programa...")
        break

    else:
        print("Opção inválida!")