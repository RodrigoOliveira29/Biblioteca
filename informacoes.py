def consultar_localizacao_contactos():
    """Exibe a localização, horário e contactos da biblioteca."""
    print("\n=== Localização e Contactos da Biblioteca ===")
    print("Morada: Rua dos Livros, nº 42, 8000-000 Faro")
    print("Coordenadas GPS: 37.0194° N, 7.9304° W")
    print("Transportes: Autocarros urbanos (Linhas 2 e 5 - Paragem 'Biblioteca Central')")
    print("Telefone: +351 289 000 000")
    print("Email: geral@biblioteca.pt")
    print("Website: www.biblioteca.pt")
    print("Horário de Funcionamento:")
    print("  - Segunda a Sexta: 09h00 às 19h30")
    print("  - Sábado: 09h30 às 13h00")
    print("  - Domingo e Feriados: Encerrado")


def consultar_regulamento():
    """Exibe o regulamento interno da biblioteca."""
    print("\n=== Regulamento da Biblioteca ===")
    print("1. Requisição de Livros e Materiais:")
    print("   - Cada leitor registado pode requisitar até 3 obras em simultâneo.")
    print("   - É obrigatória a apresentação do cartão de leitor ou identificação válida.")
    print("2. Prazos e Devoluções:")
    print("   - O prazo normal de empréstimo é de 15 dias seguidos.")
    print("   - É possível renovar o empréstimo por mais 7 dias, caso não haja reservas.")
    print("   - O atraso na devolução implica a suspensão temporária de novas requisições.")
    print("3. Utilização dos Espaços e Serviços:")
    print("   - Deve manter-se o silêncio nas salas de leitura e estudo.")
    print("   - Não é permitido consumir alimentos ou bebidas (exceto água) nas zonas de consulta.")
    print("   - Os equipamentos informáticos destinam-se exclusivamente a fins educativos e de pesquisa.")


def menu_informacoes():
    """Menu de consulta de informações gerais e regulamento da biblioteca."""
    while True:
        print("\n=== Informações e Regulamento ===")
        print("1. Localização e contactos")
        print("2. Regulamento da biblioteca")
        print("0. Voltar ao menu principal")

        opcao = input("Escolhe uma opção: ").strip()

        if opcao == "1":
            consultar_localizacao_contactos()
        elif opcao == "2":
            consultar_regulamento()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tenta novamente.")