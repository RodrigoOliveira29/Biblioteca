from utilizadores import (
    criar_conta,
    iniciar_sessao,
    terminar_sessao,
    alterar_dados_pessoais,
    eliminar_conta
)

def main():
    lista_utilizadores = []
    utilizador_atual = None

    while True:
        print("\n=== Bem-vindo à Biblioteca ===")
        if utilizador_atual:
            print(f"👤 Utilizador ligado: {utilizador_atual['username']} ({utilizador_atual['nome']})")
        else:
            print("👤 Estado: Sem sessão iniciada")
            
        print("1. Criar conta")
        print("2. Iniciar sessão")
        
        if utilizador_atual:
            print("3. Terminar sessão")
            print("4. Alterar dados pessoais")
            print("5. Eliminar conta")
            
        print("0. Sair")
        
        opcao = input("Escolhe uma opção: ").strip()

        if opcao == "1":
            criar_conta(lista_utilizadores)
        elif opcao == "2":
            if utilizador_atual:
                print("Já tens uma sessão iniciada! Termina sessão primeiro.")
            else:
                utilizador_atual = iniciar_sessao(lista_utilizadores)
        elif opcao == "3" and utilizador_atual:
            utilizador_atual = terminar_sessao(utilizador_atual)
        elif opcao == "4" and utilizador_atual:
            alterar_dados_pessoais(utilizador_atual)
        elif opcao == "5" and utilizador_atual:
            utilizador_atual = eliminar_conta(utilizador_atual, lista_utilizadores)
        elif opcao == "0":
            print("A sair da aplicação. Até logo!")
            break
        else:
            print("Opção inválida ou não disponível neste estado.")

if __name__ == "__main__":
    main()