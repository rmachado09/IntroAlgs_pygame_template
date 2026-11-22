from src.logica_jogo import mover_jogador, quebrar_texto
from src.temp_integracao import pontos_por_acao, perde_vida, separar_posts_no_chao


def test_mover_jogador_dentro_dos_limites():
    """Deve mover o jogador normalmente quando ele está longe das bordas."""
    assert mover_jogador(100, 1, 6, 800, 60) == 106


def test_mover_jogador_nao_passa_da_borda_direita():
    """Não deve permitir que o jogador saia da borda direita da tela."""
    assert mover_jogador(745, 1, 10, 800, 60) == 740


def test_mover_jogador_nao_passa_da_borda_esquerda():
    """Não deve permitir que o jogador saia da borda esquerda da tela."""
    assert mover_jogador(5, -1, 10, 800, 60) == 0


def test_quebrar_texto_em_poucas_linhas():
    """Deve quebrar um texto longo em linhas que respeitam o limite de caracteres."""
    linhas = quebrar_texto("Prefeitura abre vagas de emprego", 15)
    assert all(len(linha) <= 15 for linha in linhas)
    assert " ".join(linhas) == "Prefeitura abre vagas de emprego"


def test_pontos_por_acao_coletar():
    """Coletar um post real soma pontos; coletar um post fake não soma nada."""
    assert pontos_por_acao("coletar", False) == 10
    assert pontos_por_acao("coletar", True) == 0


def test_pontos_por_acao_atirar():
    """Atirar no fake soma pontos; atirar no real é uma acusação injusta."""
    assert pontos_por_acao("atirar", True) == 15
    assert pontos_por_acao("atirar", False) == -10


def test_perde_vida_coletar_fake_e_chao_fake():
    """O jogador perde vida ao coletar um fake ou deixar um fake chegar ao chão."""
    assert perde_vida("coletar", True) is True
    assert perde_vida("chao", True) is True
    assert perde_vida("coletar", False) is False
    assert perde_vida("atirar", True) is False


def test_separar_posts_no_chao():
    """Deve separar os posts que já passaram do fundo da tela dos que ainda estão nela."""
    import pygame

    post_na_tela = {"texto": "a", "fake": False, "pista": "p", "rect": pygame.Rect(0, 100, 220, 60)}
    post_no_chao = {"texto": "b", "fake": True, "pista": "p", "rect": pygame.Rect(0, 610, 220, 60)}

    restantes, no_chao = separar_posts_no_chao([post_na_tela, post_no_chao], 600)

    assert restantes == [post_na_tela]
    assert no_chao == [post_no_chao]
