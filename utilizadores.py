def criar_conta(lista_utilizadores):
    """Permite criar uma nova conta de utilizador."""
    print("\n=== Criar Conta ===")
    username = input("Escolhe um nome de utilizador: ").strip()
    
    if not username:
        print("Erro: O nome de utilizador não pode estar vazio.")
        return False

    if any(u.get('username') == username for u in lista_utilizadores):
        print("Erro: Esse nome de utilizador já existe.")
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
    print(f"Sucesso! Conta de '{username}' criada com sucesso.")
    return True


def iniciar_sessao(lista_utilizadores):
    """Permite iniciar sessão na aplicação."""
    print("\n=== Iniciar Sessão ===")
    if not lista_utilizadores:
        print("Aviso: Ainda não existem contas criadas no sistema.")
        return None

    username = input("Nome de utilizador: ").strip()
    password = input("Palavra-passe: ").strip()

    for utilizador in lista_utilizadores:
        if utilizador.get('username') == username and utilizador.get('password') == password:
            print(f"Sessão iniciada com sucesso. Bem-vindo(a), {utilizador.get('nome', username)}!")
            return utilizador

    print("Erro: Utilizador ou palavra-passe incorretos.")
    return None


def terminar_sessao(utilizador_atual):
    """Termina a sessão atual."""
    if utilizador_atual is None:
        print("\nNão tens nenhuma sessão iniciada.")
        return None
    
    print(f"\nSessão terminada com sucesso para o utilizador: {utilizador_atual.get('username')}.")
    return None