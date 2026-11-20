favoritos_db = {}

def adicionar_favorito(username):
    """Permite ao leitor guardar um livro nos favoritos."""
    print("\n--- Adicionar aos Favoritos ---")
    livro = input("Insere o título do livro que queres guardar: ").strip()
    
    if not livro:
        print("Erro: O título do livro não pode estar vazio.")
        return

    # Se o utilizador ainda não tiver registo nos favoritos, cria uma lista vazia
    if username not in favoritos_db:
        favoritos_db[username] = []
    
    # Verifica se o livro já existe na lista
    if livro in favoritos_db[username]:
        print(f"O livro '{livro}' já consta nos teus favoritos.")
    else:
        favoritos_db[username].append(livro)
        print(f"Livro '{livro}' adicionado aos favoritos com sucesso!")

def consultar_favoritos(username):
    """Permite ao leitor consultar a sua lista de livros favoritos."""
    print(f"\n--- Os Teus Livros Favoritos ---")
    
    if username not in favoritos_db or not favoritos_db[username]:
        print("Ainda não tens nenhum livro guardado nos favoritos.")
        return
    
    # Mostra a lista numerada de livros
    for i, livro in enumerate(favoritos_db[username], 1):
        print(f"{i}. {livro}")

if __name__ == "__main__":
    utilizador_teste = "rodrigo"  # Simula um utilizador com sessão iniciada
    
    while True:
        print("\n=== MENU DE TESTE: FAVORITOS ===")
        print("1. Guardar livro nos favoritos")
        print("2. Consultar lista de favoritos")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_favorito(utilizador_teste)
        elif opcao == "2":
            consultar_favoritos(utilizador_teste)
        elif opcao == "0":
            print("A sair do teste...")
            break
        else:
            print("Opção inválida. Tenta novamente.")