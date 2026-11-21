from informacoes import menu_informacoes
from Requisicoes import menu_requisicoes, verificar_avisos_utilizador
from catalogo import menu_catalogo
from favoritos import menu_favoritos
from prazos import menu_prazos
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
            elif opcao == "0":
                print("A sair da aplicação. Até logo!")
                break
            else:
                print("Opção inválida.")

        else:
            print(f"👤 Utilizador ligado: {utilizador_atual['username']} ({utilizador_atual['nome']})")
            verificar_avisos_utilizador(dias_aviso=3, mostrar_se_vazio=False)
            print()
            print("1. Catálogo")
            print("2. Requisições")
            print("3. Favoritos")
            print("4. Prazos")
            print("5. Conta")
            print("6. Informações")
            print("0. Sair")

            opcao = input("Escolhe uma opção: ").strip()

            if opcao == "1":
                menu_catalogo()
            elif opcao == "2":
                menu_requisicoes()
            elif opcao == "3":
                menu_favoritos(utilizador_atual['username'])
            elif opcao == "4":
                menu_prazos()
            elif opcao == "5":
                utilizador_atual = menu_conta(utilizador_atual, lista_utilizadores)
            elif opcao == "6":
                menu_informacoes()
            elif opcao == "0":
                print("A sair da aplicação. Até logo!")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    main()