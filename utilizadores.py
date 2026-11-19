def criar_conta(lista_utilizadores):
    """
    Permite criar uma nova conta de utilizador na aplicação.
    Guarda os dados num dicionário e adiciona-o à lista global de utilizadores.
    """
    print("\n=== Criar Conta na Biblioteca ===")
    
    username = input("Escolhe um nome de utilizador: ").strip()
    
    if not username:
        print("Erro: O nome de utilizador não pode estar vazio.")
        return False

    if any(u.get('username') == username for u in lista_utilizadores):
        print("Erro: Esse nome de utilizador já está a ser utilizado.")
        return False

    password = input("Escolhe uma palavra-passe: ").strip()
    if not password:
        print("Erro: A palavra-passe não pode estar vazia.")
        return False

    nome = input("Introduz o teu nome completo: ").strip()
    email = input("Introduz o teu e-mail: ").strip()

    novo_utilizador = {
        "username": username,
        "password": password,
        "nome": nome,
        "email": email,
        "historico": []
    }
    
    lista_utilizadores.append(novo_utilizador)
    print(f"\nSucesso! Conta de '{username}' criada com sucesso.")
    return True


if __name__ == "__main__":
    base_dados_exemplo = []
    
    criar_conta(base_dados_exemplo)
    
    print("\n--- Estado atual da base de dados ---")
    print(base_dados_exemplo)