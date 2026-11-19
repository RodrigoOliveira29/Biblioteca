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
    """Mostra os livros cujo título tem o texto procurado."""
    obras = consultar_catalogo(catalogo)
    termo = titulo.strip().lower()

    if not termo:
        return []

    resultados = []
    for livro in obras:
        if termo in livro.get("titulo", "").lower():
            resultados.append(livro)

    return resultados


def menu_catalogo() -> None:
    """Mostra um menu para realizar as opções disponíveis."""
    while True:
        print("\n=== MENU CATÁLOGO ===")
        print("1 - Consultar catálogo completo")
        print("2 - Pesquisar livro por título")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolhe uma opção: ").strip()

        if opcao == "1":
            mostrar_catalogo()
            input("\nPressiona ENTER para continuar...")
        elif opcao == "2":
            termo = input("Escreve o título a pesquisar: ")
            resultados = pesquisar_por_titulo(termo)
            mostrar_catalogo(resultados)
            input("\nPressiona ENTER para continuar...")
        elif opcao == "0":
            print("A voltar ao menu principal...")
            return
        else:
            print("Opção inválida. Tenta novamente.")


if __name__ == "__main__":
    menu_catalogo()