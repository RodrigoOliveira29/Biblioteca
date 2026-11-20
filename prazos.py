from datetime import date


def calcular_dias_restantes(data_limite: date, data_referencia: date | None = None) -> int:
    """Calcula quantos dias faltam até à data limite (negativo se já passou)."""
    hoje = data_referencia or date.today()
    return (data_limite - hoje).days


def obter_avisos_prazo(
    requisicoes_ativas: list[dict],
    dias_aviso: int = 3,
    data_referencia: date | None = None,
) -> list[dict]:
    """Devolve alertas para empréstimos com prazo próximo ou ultrapassado."""
    avisos = []

    for req in requisicoes_ativas:
        data_limite = req.get("data_limite")
        if not isinstance(data_limite, date):
            continue

        dias_restantes = calcular_dias_restantes(data_limite, data_referencia)

        if dias_restantes < 0:
            estado = "atrasado"
            mensagem = (
                f"⚠️ ATRASO: O livro '{req['titulo']}' está fora do prazo há "
                f"{abs(dias_restantes)} dia(s) (limite: {data_limite})."
            )
        elif dias_restantes == 0:
            estado = "hoje"
            mensagem = (
                f"⚠️ AVISO: O livro '{req['titulo']}' tem data limite de devolução HOJE ({data_limite})."
            )
        elif dias_restantes <= dias_aviso:
            estado = "proximo"
            mensagem = (
                f"⚠️ AVISO: Faltam {dias_restantes} dia(s) para devolver '{req['titulo']}' "
                f"(limite: {data_limite})."
            )
        else:
            continue

        avisos.append({
            "requisicao": req,
            "dias_restantes": dias_restantes,
            "estado": estado,
            "mensagem": mensagem,
        })

    return avisos


def mostrar_avisos_devolucao(
    requisicoes_ativas: list[dict],
    dias_aviso: int = 3,
    data_referencia: date | None = None,
    mostrar_se_vazio: bool = False,
) -> None:
    """Imprime os avisos de devolução no terminal."""
    avisos = obter_avisos_prazo(
        requisicoes_ativas,
        dias_aviso=dias_aviso,
        data_referencia=data_referencia,
    )

    if not avisos:
        if mostrar_se_vazio:
            print("\n✅ Sem avisos de devolução próximos.")
        return

    print("\n=== AVISOS DE DEVOLUÇÃO ===")
    for aviso in avisos:
        print(aviso["mensagem"])


def mostrar_resumo_prazos(
    requisicoes_ativas: list[dict],
    dias_aviso: int = 3,
    data_referencia: date | None = None,
    mostrar_se_vazio: bool = False,
) -> None:
    """Mostra quanto tempo falta para cada livro e ativa os avisos quando o prazo está perto."""
    if not requisicoes_ativas:
        if mostrar_se_vazio:
            print("\nNão tens livros requisitados de momento.")
        return

    print("\n--- PRAZOS DE DEVOLUÇÃO ---")
    for req in requisicoes_ativas:
        data_limite = req.get("data_limite")
        if not isinstance(data_limite, date):
            continue

        dias = calcular_dias_restantes(data_limite, data_referencia)
        if dias > 1:
            print(f"• {req['titulo']}: faltam {dias} dias (limite: {data_limite})")
        elif dias == 1:
            print(f"• {req['titulo']}: falta 1 dia (limite: {data_limite})")
        elif dias == 0:
            print(f"• {req['titulo']}: termina hoje (limite: {data_limite})")
        else:
            print(f"• {req['titulo']}: atrasado há {abs(dias)} dia(s) (limite: {data_limite})")

    mostrar_avisos_devolucao(
        requisicoes_ativas,
        dias_aviso=dias_aviso,
        data_referencia=data_referencia,
        mostrar_se_vazio=False,
    )