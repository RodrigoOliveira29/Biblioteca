def criar_conta(lista_utilizadores):
    """Permite criar uma nova conta de utilizador (podes escrever '0' para cancelar)."""
    print("\n=== Criar Conta (Podes escrever '0' para cancelar) ===")
    
    username = input("Escolhe um nome de utilizador (ou '0' para cancelar): ").strip()
    if username == "0":
        print("Operação cancelada.")
        return False
    
    if not username:
        print("Erro: O nome de utilizador não pode estar vazio.")
        return False

    if any(u.get('username') == username for u in lista_utilizadores):
        print("Erro: Esse nome de utilizador já existe.")
        return False

    nome = input("Introduz o teu nome completo (ou '0' para cancelar): ").strip()
    if nome == "0":
        print("Operação cancelada.")
        return False

    while True:
        email = input("Introduz o teu e-mail (ou '0' para cancelar): ").strip()
        if email == "0":
            print("Operação cancelada.")
            return False
        if "@" in email:
            break
        print("Erro: O e-mail tem de conter obrigatoriamente o símbolo '@'. Tenta novamente.")

    password = input("Escolhe uma palavra-passe (ou '0' para cancelar): ").strip()
    if password == "0":
        print("Operação cancelada.")
        return False
    if not password:
        print("Erro: A palavra-passe não pode estar vazia.")
        return False

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
    """Permite iniciar sessão na aplicação (podes escrever '0' para cancelar)."""
    print("\n=== Iniciar Sessão (Podes escrever '0' para cancelar) ===")
    if not lista_utilizadores:
        print("Aviso: Ainda não existem contas criadas no sistema.")
        return None

    username = input("Nome de utilizador (ou '0' para cancelar): ").strip()
    if username == "0":
        print("Operação cancelada.")
        return None

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
    """Permite alterar os dados pessoais do utilizador com sessão ativa."""
    if utilizador_atual is None:
        print("\nErro: Tens de iniciar sessão primeiro para poderes alterar os teus dados.")
        return False

    print(f"\n=== Alterar Dados Pessoais ({utilizador_atual.get('username')}) ===")
    print("1. Alterar Nome")
    print("2. Alterar E-mail")
    print("3. Alterar Palavra-passe")
    print("0. Voltar / Cancelar")
    
    opcao = input("Escolhe uma opção: ").strip()

    if opcao == "1":
        novo_nome = input("Introduz o novo nome completo (ou '0' para cancelar): ").strip()
        if novo_nome == "0":
            print("Operação cancelada.")
            return
        if novo_nome:
            utilizador_atual['nome'] = novo_nome
            print("Nome alterado com sucesso!")
        else:
            print("Erro: O nome não pode estar vazio.")
            
    elif opcao == "2":
        while True:
            novo_email = input("Introduz o novo e-mail (ou '0' para cancelar): ").strip()
            if novo_email == "0":
                print("Operação cancelada.")
                return
            if "@" in novo_email:
                utilizador_atual['email'] = novo_email
                print("E-mail alterado com sucesso!")
                break
            print("Erro: O e-mail tem de conter obrigatoriamente o símbolo '@'. Tenta novamente.")
            
    elif opcao == "3":
        nova_pass = input("Introduz a nova palavra-passe (ou '0' para cancelar): ").strip()
        if nova_pass == "0":
            print("Operação cancelada.")
            return
        if nova_pass:
            utilizador_atual['password'] = nova_pass
            print("Palavra-passe alterada com sucesso!")
        else:
            print("Erro: A palavra-passe não pode estar vazia.")
            
    elif opcao == "0":
        print("Operação cancelada.")
    else:
        print("Opção inválida.")


def eliminar_conta(utilizador_atual, lista_utilizadores):
    """Permite ao utilizador solicitar e efetuar a eliminação da sua própria conta."""
    if utilizador_atual is None:
        print("\nErro: Tens de iniciar sessão primeiro.")
        return None

    print(f"\n=== Eliminar Conta ({utilizador_atual.get('username')}) ===")
    confirmacao = input("Tens a certeza absoluta que queres eliminar a tua conta? Esta ação é irreversível (s/n): ").strip().lower()

    if confirmacao == 's':
        lista_utilizadores.remove(utilizador_atual)
        print("A tua conta foi eliminada com sucesso. A terminar sessão...")
        return None
    
    print("Operação cancelada. A tua conta está segura.")
    return utilizador_atual