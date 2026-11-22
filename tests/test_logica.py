import pytest

from src.funcoes import (
    PENALIDADE_ACUSACAO_INJUSTA,
    PONTOS_COLETAR_REAL,
    PONTOS_ELIMINAR_FAKE,
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    perde_vida,
    pontos_por_acao,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


# --- Regras de pontuação por ação ---

def test_pontos_por_acao_coletar_real_da_10():
    """Coletar um post real vale +10."""
    assert pontos_por_acao("coletar", False) == 10


def test_pontos_por_acao_coletar_fake_nao_da_pontos():
    """Coletar um post falso não pontua (o custo é a vida)."""
    assert pontos_por_acao("coletar", True) == 0


def test_pontos_por_acao_atirar_fake_da_15():
    """Eliminar um post falso com o Selo FAKE vale +15."""
    assert pontos_por_acao("atirar", True) == 15


def test_pontos_por_acao_atirar_real_tira_10():
    """Acusar um post real com o Selo FAKE (acusação injusta) vale -10."""
    assert pontos_por_acao("atirar", False) == -10


def test_pontos_por_acao_chao_nao_pontua():
    """Post no chão, real ou falso, não muda a pontuação."""
    assert pontos_por_acao("chao", False) == 0
    assert pontos_por_acao("chao", True) == 0


def test_pontos_por_acao_usa_as_constantes_do_jogo():
    """Os valores batem com as constantes PONTOS_* e PENALIDADE_*."""
    assert pontos_por_acao("coletar", False) == PONTOS_COLETAR_REAL
    assert pontos_por_acao("atirar", True) == PONTOS_ELIMINAR_FAKE
    assert pontos_por_acao("atirar", False) == PENALIDADE_ACUSACAO_INJUSTA


def test_pontos_por_acao_acao_desconhecida_levanta_erro():
    """Uma ação fora de coletar/atirar/chao levanta ValueError."""
    with pytest.raises(ValueError):
        pontos_por_acao("pular", False)
    with pytest.raises(ValueError):
        pontos_por_acao("", True)


def test_pontos_por_acao_combina_com_calcular_pontos():
    """A acusação injusta, somada ao placar, desconta 10 pontos."""
    assert calcular_pontos(30, pontos_por_acao("atirar", False)) == 20


# --- Regras de perda de vida ---

def test_perde_vida_ao_coletar_fake():
    """Coletar um post falso custa 1 vida."""
    assert perde_vida("coletar", True) is True


def test_perde_vida_quando_fake_chega_ao_chao():
    """Deixar um post falso chegar ao chão custa 1 vida."""
    assert perde_vida("chao", True) is True


def test_nao_perde_vida_ao_coletar_real():
    """Coletar um post real é seguro."""
    assert perde_vida("coletar", False) is False


def test_nao_perde_vida_quando_real_chega_ao_chao():
    """Post real no chão não tem penalidade."""
    assert perde_vida("chao", False) is False


def test_nao_perde_vida_ao_atirar():
    """Atirar, acertando fake ou real, não custa vida (só muda os pontos)."""
    assert perde_vida("atirar", True) is False
    assert perde_vida("atirar", False) is False