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
    
    while True:
        email = input("Introduz o teu e-mail: ").strip()
        if "@" in email:
            break
        print("Erro: O e-mail tem de conter obrigatoriamente o símbolo '@'. Tenta novamente.")

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

def alterar_dados_pessoais(utilizador_atual):
    """Permite alterar os dados pessoais (nome, e-mail e palavra-passe) do utilizador com sessão ativa."""
    if utilizador_atual is None:
        print("\nErro: Tens de iniciar sessão primeiro para poderes alterar os teus dados.")
        return False

    print(f"\n=== Alterar Dados Pessoais ({utilizador_atual.get('username')}) ===")
    print("1. Alterar Nome")
    print("2. Alterar E-mail")
    print("3. Alterar Palavra-passe")
    print("0. Voltar")
    
    opcao = input("Escolhe uma opção: ").strip()

    if opcao == "1":
        novo_nome = input("Introduz o novo nome completo: ").strip()
        if novo_nome:
            utilizador_atual['nome'] = novo_nome
            print("Nome alterado com sucesso!")
        else:
            print("Erro: O nome não pode estar vazio.")
            
    elif opcao == "2":
        while True:
            novo_email = input("Introduz o novo e-mail: ").strip()
            if "@" in novo_email:
                utilizador_atual['email'] = novo_email
                print("E-mail alterado com sucesso!")
                break
            print("Erro: O e-mail tem de conter obrigatoriamente o símbolo '@'. Tenta novamente.")
            
    elif opcao == "3":
        nova_pass = input("Introduz a nova palavra-passe: ").strip()
        if nova_pass:
            utilizador_atual['password'] = nova_pass
            print("Palavra-passe alterada com sucesso!")
        else:
            print("Erro: A palavra-passe não pode estar vazia.")
            
    elif opcao == "0":
        print("Operação cancelada.")
    else:
        print("Opção inválida.")