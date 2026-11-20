from datetime import date, timedelta
from catalogo import CATALOGO_LIVROS
from prazos import mostrar_resumo_prazos

# Lista de requisições ativas
requisicoes = []

# Histórico de requisições
historico = []


# Mostrar livros disponíveis
def mostrar_livros():
    print("\n--- LIVROS DISPONÍVEIS ---")
    disponiveis = [livro for livro in CATALOGO_LIVROS if livro.get("disponivel")]

    if not disponiveis:
        print("Não existem livros disponíveis de momento.")
        return

    for livro in disponiveis:
        print(f"{livro['id']} - {livro['titulo']} ({livro['autor']})")


# Requisitar um livro
def requisitar_livro():
    mostrar_livros()

    try:
        id_livro = int(input("\nIndica o ID do livro: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    for livro in CATALOGO_LIVROS:
        if livro["id"] == id_livro:
            if livro.get("disponivel"):
                data_inicio = date.today()
                data_limite = data_inicio + timedelta(days=14)

                nova_requisicao = {
                    "id_livro": livro["id"],
                    "titulo": livro["titulo"],
                    "data_requisicao": data_inicio,
                    "data_limite": data_limite,
                }

                requisicoes.append(nova_requisicao)
                livro["disponivel"] = False

                print("\nLivro requisitado com sucesso!")
                print("Data limite de devolução:", data_limite)
            else:
                print("Este livro já está requisitado.")
            return

    print("Livro não encontrado.")


# Consultar livros requisitados
def consultar_requisicoes():
    print("\n--- LIVROS REQUISITADOS ---")

    if not requisicoes:
        print("Não tens livros requisitados.")
        return

    for req in requisicoes:
        print("Livro:", req["titulo"])
        print("Data limite:", req["data_limite"])
        print("-------------------------")


# Consultar datas limite
def consultar_datas():
    print("\n--- DATAS DE DEVOLUÇÃO ---")

    if not requisicoes:
        print("Não tens livros requisitados.")
        return

    for req in requisicoes:
        print(req["titulo"], "-", req["data_limite"])


# Devolver um livro
def devolver_livro():
    consultar_requisicoes()

    if not requisicoes:
        return

    termo = input("\nIndica o nome do livro a devolver: ").strip().lower()

    for req in list(requisicoes):
        if req["titulo"].strip().lower() == termo:
            req["data_devolucao"] = date.today()
            historico.append(req.copy())
            requisicoes.remove(req)

            for livro in CATALOGO_LIVROS:
                if livro["id"] == req.get("id_livro") or livro["titulo"].strip().lower() == termo:
                    livro["disponivel"] = True

            print("Livro devolvido com sucesso!")
            return

    print("Não tens esse livro requisitado.")


# Consultar histórico
def consultar_historico():
    print("\n--- HISTÓRICO DE REQUISIÇÕES ---")

    if not historico:
        print("Ainda não existem requisições anteriores.")
        return

    for reg in historico:
        print("Livro:", reg["titulo"])
        print("Requisitado em:", reg["data_requisicao"])
        print("Devolvido em:", reg["data_devolucao"])
        print("-------------------------")


def verificar_avisos_utilizador(dias_aviso: int = 3, mostrar_se_vazio: bool = False):
    """Mostra o tempo restante e dispara avisos quando o prazo está perto."""
    mostrar_resumo_prazos(
        requisicoes,
        dias_aviso=dias_aviso,
        mostrar_se_vazio=mostrar_se_vazio,
    )


def menu_requisicoes():
    verificar_avisos_utilizador(dias_aviso=3, mostrar_se_vazio=False)

    while True:
        print("\n===== REQUISIÇÕES =====")
        print("1 - Mostrar livros disponíveis")
        print("2 - Requisitar livro")
        print("3 - Consultar livros requisitados")
        print("4 - Consultar datas de devolução")
        print("5 - Devolver livro")
        print("6 - Consultar histórico")
        print("0 - Voltar")

        opcao = input("\nEscolhe uma opção: ").strip()

        if opcao == "1":
            mostrar_livros()
            input("\nPressiona ENTER para continuar...")
        elif opcao == "2":
            requisitar_livro()
            input("\nPressiona ENTER para continuar...")
        elif opcao == "3":
            consultar_requisicoes()
            input("\nPressiona ENTER para continuar...")
        elif opcao == "4":
            consultar_datas()
            input("\nPressiona ENTER para continuar...")
        elif opcao == "5":
            devolver_livro()
            input("\nPressiona ENTER para continuar...")
        elif opcao == "6":
            consultar_historico()
            input("\nPressiona ENTER para continuar...")
        elif opcao == "0":
            print("A voltar...")
            break
        else:
            print("Opção inválida!")
            input("\nPressiona ENTER para continuar...")


if __name__ == "__main__":
    menu_requisicoes()