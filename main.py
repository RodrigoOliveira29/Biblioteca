from catalogo import menu_catalogo
from Requisicoes import menu_requisicoes, verificar_avisos_utilizador
from utilizadores import (
    criar_conta,
    iniciar_sessao,
    terminar_sessao,
    alterar_dados_pessoais,
    eliminar_conta,
)


def menu_conta(utilizador_atual, lista_utilizadores):
    while True:
        print(f"\n=== Gestão de Conta ({utilizador_atual['username']}) ===")
        print("1. Alterar dados pessoais")
        print("2. Terminar sessão")
        print("3. Eliminar conta")
        print("0. Voltar ao menu principal")

        opcao = input("Escolhe uma opção: ").strip()

        if opcao == "1":
            alterar_dados_pessoais(utilizador_atual)
        elif opcao == "2":
            return terminar_sessao(utilizador_atual)
        elif opcao == "3":
            return eliminar_conta(utilizador_atual, lista_utilizadores)
        elif opcao == "0":
            return utilizador_atual
        else:
            print("Opção inválida.")


def main():
    lista_utilizadores = []
    utilizador_atual = None

    while True:
        print("\n=== Bem-vindo à Biblioteca ===")

        # Menu quando NÃO há sessão iniciada
        if not utilizador_atual:
            print("👤 Estado: Sem sessão iniciada")
            print("1. Criar conta")
            print("2. Iniciar sessão")
            print("0. Sair")

            opcao = input("Escolhe uma opção: ").strip()

            if opcao == "1":
                criar_conta(lista_utilizadores)
            elif opcao == "2":
                utilizador_atual = iniciar_sessao(lista_utilizadores)
                if utilizador_atual:
                    verificar_avisos_utilizador(dias_aviso=3, mostrar_se_vazio=False)
            elif opcao == "0":
                print("A sair da aplicação. Até logo!")
                break
            else:
                print("Opção inválida.")

        # Menu quando HÁ sessão iniciada
        else:
            print(f"👤 Utilizador ligado: {utilizador_atual['username']} ({utilizador_atual['nome']})")
            verificar_avisos_utilizador(dias_aviso=3, mostrar_se_vazio=False)
            print()
            print("1. Catálogo")
            print("2. Conta")
            print("3. Requisições")
            print("4. Prazos")
            print("0. Sair")

            opcao = input("Escolhe uma opção: ").strip()

            if opcao == "1":
                menu_catalogo()
            elif opcao == "2":
                utilizador_atual = menu_conta(utilizador_atual, lista_utilizadores)
            elif opcao == "3":
                menu_requisicoes()
            elif opcao == "4":
                verificar_avisos_utilizador(dias_aviso=3, mostrar_se_vazio=True)
                input("\nPressiona ENTER para continuar...")
            elif opcao == "0":
                print("A sair da aplicação. Até logo!")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    main()