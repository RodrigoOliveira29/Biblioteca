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