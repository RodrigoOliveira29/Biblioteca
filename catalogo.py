CATALOGO_LIVROS = [
    {
        "id": 1,
        "titulo": "Os Lusíadas",
        "autor": "Luís de Camões",
        "genero": "Epopeia",
        "ano": 1572,
        "disponivel": True,
        "descricao": "Os Lusíadas é uma epopeia de Luís Vaz de Camões, publicada em 1572, que celebra os grandes feitos do povo português, com foco na viagem marítima de Vasco da Gama à Índia."
        "Dividida em dez cantos, a obra entrelaça factos históricos e mitologia clássica, onde os deuses do Olimpo — como Vénus, protetora dos portugueses, e Baco, seu opositor — decidem o destino da expedição. "
        "Ao longo da narrativa, Camões exalta a coragem dos navegadores e recorda episódios marcantes da história de Portugal, como a história de Inês de Castro e a Batalha de Aljubarrota, mas também deixa avisos "
        "críticos sobre a ambição desmedida, a ganância e a decadência do império, simbolizados por figuras como o Velho do Restelo e o gigante Adamastor.",
    },
    {
        "id": 2,
        "titulo": "Mensagem",
        "autor": "Fernando Pessoa",
        "genero": "Poesia",
        "ano": 1934,
        "disponivel": True,
        "descricao": "Mensagem é o único livro de poemas em português publicado em vida por Fernando Pessoa, em 1934, que reinterpreta de forma mítica e simbólica a história de Portugal. "
        "Organizada em três partes (Brasão, Mar Português e O Encoberto), a obra percorre a ascensão, a glória dos Descobrimentos e a decadência do país, transformando figuras históricas como D. "
        "Sebastião, Infante D. Henrique ou Vasco da Gama em símbolos espirituais. Em vez de celebrar apenas o passado material, Pessoa apela à regeneração nacional através de um império cultural "
        "e espiritual, culminando na profecia messiânica do Quinto Império e na célebre frase 'Tudo vale a pena se a alma não é pequena.'",
    },
    {
        "id": 3,
        "titulo": "Memorial do Convento",
        "autor": "José Saramago",
        "genero": "Romance",
        "ano": 1982,
        "disponivel": True,
        "descricao": "Memorial do Convento é um romance histórico de José Saramago, publicado em 1982, que mistura factos reais e ficção no Portugal absolutista do início do século XVIII."
        "A história acompanha a promessa do rei D. João V de erguer um grandioso convento em Mafra caso consiga ter um herdeiro com a rainha D. Maria Ana, revelando o contraste extremo entre "
        "o luxo da corte e o sofrimento do povo forçado a trabalhar na obra. Em paralelo, desenrola-se a história de amor e cumplicidade entre Baltazar Sete-Sóis, um ex-soldado sem a mão esquerda, "
        "e Blimunda Sete-Luas, uma mulher dotada do dom de ver o interior das pessoas quando está em jejum. Juntos, auxiliam o padre Bartolomeu de Gusmão na construção da passarola, uma máquina voadora "
        "movida pelas vontades humanas recolhidas por Blimunda, enquanto enfrentam a perseguição implacável da Inquisição.",
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
    titulo: str, catalogo: list[dict] | None = None) -> list[dict]:
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


def pesquisar_por_autor(
    autor: str, catalogo: list[dict] | None = None) -> list[dict]:
    """Devolve os livros cujo autor contém o texto pesquisado."""
    obras = consultar_catalogo(catalogo)
    termo = autor.strip().lower()

    if not termo:
        return []

    resultados = []
    for livro in obras:
        if termo in livro.get("autor", "").lower():
            resultados.append(livro)

    return resultados


def obter_detalhes_por_titulo(
    titulo: str, catalogo: list[dict] | None = None) -> list[dict]:
    """Devolve os livros cujo título corresponde à pesquisa."""
    return pesquisar_por_titulo(titulo, catalogo)


def mostrar_detalhes_livro(
    titulo: str, catalogo: list[dict] | None = None) -> None:
    """Mostra os detalhes do livro pesquisado pelo título."""
    livros = obter_detalhes_por_titulo(titulo, catalogo)
    if not livros:
        print(f"\nNão foi encontrado nenhum livro com o título '{titulo}'.")
        return

    for livro in livros:
        estado = "Disponível" if livro.get("disponivel") else "Indisponível"
        print("\n=== DETALHES DO LIVRO ===")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Editora: {livro.get('editora', 'Não especificada')}")
        print(f"Ano de publicação: {livro['ano']}")
        print(f"Género: {livro['genero']}")
        print(f"Estado: {estado}")
        print(f"Descrição: {livro.get('descricao', 'Sem descrição disponível.')}")



def menu_catalogo() -> None:
    """Mostra um menu para realizar as opções disponíveis."""
    while True:
        print("\n=== MENU CATÁLOGO ===")
        print("1 - Consultar catálogo completo")
        print("2 - Pesquisar livro por título")
        print("3 - Pesquisar livro por autor")
        print("4 - Consultar detalhes de um livro")
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
        elif opcao == "3":
            termo = input("Escreve o nome do autor a pesquisar: ")
            resultados = pesquisar_por_autor(termo)
            mostrar_catalogo(resultados)
            input("\nPressiona ENTER para continuar...")
        elif opcao == "4":
            titulo = input("Escreve o título do livro: ").strip()
            mostrar_detalhes_livro(titulo)
            input("\nPressiona ENTER para continuar...")
        elif opcao == "0":
            print("A voltar ao menu principal...")
            return
        else:
            print("Opção inválida. Tenta novamente.")


if __name__ == "__main__":
    menu_catalogo()