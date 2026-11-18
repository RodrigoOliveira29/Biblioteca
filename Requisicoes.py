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