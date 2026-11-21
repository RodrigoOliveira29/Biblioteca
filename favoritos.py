from catalogo import CATALOGO_LIVROS

favoritos_db = {}

def adicionar_favorito(username):
    """Permite ao leitor guardar um livro nos favoritos, com opção de voltar atrás."""
    print("\n--- Adicionar aos Favoritos ---")
    
    if username not in favoritos_db:
        favoritos_db[username] = []
    
    livros_disponiveis_para_favorito = [
        livro for livro in CATALOGO_LIVROS 
        if livro["titulo"] not in favoritos_db[username]
    ]
    
    if not livros_disponiveis_para_favorito:
        print("\nJá tens todos os livros do catálogo guardados nos favoritos!")
        return

    print("\nLivros disponíveis que ainda não tens nos favoritos:")
    for livro in livros_disponiveis_para_favorito:
        print(f"[{livro['id']}] {livro['titulo']} — {livro['autor']}")
    
    print("[0] Voltar atrás")
    
    entrada = input("\nInsere o ID do livro que queres guardar (ou 0 para voltar): ").strip()
    
    # Opção para voltar atrás
    if entrada == "0":
        print("A voltar ao menu anterior...")
        return
    
    if not entrada.isdigit():
        print("Erro: O ID tem de ser um número válido.")
        return

    livro_id = int(entrada)
    
    livro_encontrado = None
    for livro in livros_disponiveis_para_favorito:
        if livro["id"] == livro_id:
            livro_encontrado = livro
            break
            
    if not livro_encontrado:
        print(f"Erro: ID inválido ou o livro com o ID {livro_id} já está nos teus favoritos.")
        return

    titulo_livro = livro_encontrado["titulo"]

    favoritos_db[username].append(titulo_livro)
    print(f"Livro '{titulo_livro}' adicionado aos favoritos com sucesso!")

def consultar_favoritos(username):
    """Permite ao leitor consultar a sua lista de livros favoritos, com opção de voltar atrás."""
    print(f"\n--- Os Teus Livros Favoritos ---")
    
    if username not in favoritos_db or not favoritos_db[username]:
        print("Ainda não tens nenhum livro guardado nos favoritos.")
        input("\nPressiona ENTER para voltar atrás...")
        return
    
    for i, livro in enumerate(favoritos_db[username], 1):
        print(f"{i}. {livro}")
    
    print("\n[0] Voltar atrás")
    opcao = input("Escolhe uma opção: ").strip()
    
    if opcao == "0":
        print("A voltar ao menu anterior...")
        return
    else:
        print("Opção inválida. A voltar ao menu anterior...")

def menu_favoritos(username):
    """Mostra o menu de gestão de favoritos do utilizador."""
    while True:
        print("\n=== MENU FAVORITOS ===")
        print("1. Adicionar livro aos favoritos")
        print("2. Consultar lista de favoritos")
        print("0. Voltar ao menu principal")
        
        opcao = input("Escolhe uma opção: ").strip()
        
        if opcao == "1":
            adicionar_favorito(username)
            input("\nPressiona ENTER para continuar...")
        elif opcao == "2":
            consultar_favoritos(username)
            input("\nPressiona ENTER para continuar...")
        elif opcao == "0":
            print("A voltar ao menu principal...")
            return
        else:
            print("Opção inválida. Tenta novamente.")