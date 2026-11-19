CATALOGO_LIVROS = [
    {
        "id": 1,
        "titulo": "Os Lusíadas",
        "autor": "Luís de Camões",
        "genero": "Epopeia",
        "ano": 1572,
        "disponivel": True,
    },
    {
        "id": 2,
        "titulo": "Mensagem",
        "autor": "Fernando Pessoa",
        "genero": "Poesia",
        "ano": 1934,
        "disponivel": True,
    },
    {
        "id": 3,
        "titulo": "Memorial do Convento",
        "autor": "José Saramago",
        "genero": "Romance",
        "ano": 1982,
        "disponivel": True,
    },
]


def consultar_catalogo(catalogo: list[dict] | None = None) -> list[dict]:
    """Vai buscar e devolve a lista de livros do catálogo."""
    if catalogo is None:
        catalogo = CATALOGO_LIVROS
    return catalogo


def mostrar_catalogo(catalogo: list[dict] | None = None) -> None:
    """Imprime os livros do catálogo no ecrã."""
    obras = consultar_catalogo(catalogo)

    if not obras:
        print("Não existem livros registados no catálogo.")
        return

    print("\n=== CATÁLOGO DE LIVROS ===")
    for livro in obras:
        estado = "Disponível" if livro.get("disponivel") else "Indisponível"
        print(
            f"[{livro['id']}] {livro['titulo']} — {livro['autor']} "
            f"({livro['ano']}) | Género: {livro['genero']} | {estado}"
        )


def pesquisar_por_titulo(
    titulo: str, catalogo: list[dict] | None = None
) -> list[dict]:
    """Devolve os livros cujo título contém o texto pesquisado."""
    obras = consultar_catalogo(catalogo)
    termo = titulo.strip().lower()

    if not termo:
        return []

    resultados = []
    for livro in obras:
        if termo in livro.get("titulo", "").lower():
            resultados.append(livro)

    return resultados


if __name__ == "__main__":
    mostrar_catalogo()
    termo = input("\nEscreve o título a pesquisar: ")
    mostrar_catalogo(pesquisar_por_titulo(termo))