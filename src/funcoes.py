# Pontos de cada ação do jogador (regras do "Fato ou Fake?").
PONTOS_COLETAR_REAL = 10
PONTOS_ELIMINAR_FAKE = 15
PENALIDADE_ACUSACAO_INJUSTA = -10

# Regras de pontuação: a chave é (ação, eh_fake) e o valor é a variação de
# pontos. Um dicionário no lugar de vários ifs deixa as regras visíveis de
# uma vez e fáceis de mudar.
REGRAS_PONTOS = {
    ("coletar", False): PONTOS_COLETAR_REAL,         # coletou post real
    ("coletar", True): 0,                            # coletou post fake: só perde vida
    ("atirar", True): PONTOS_ELIMINAR_FAKE,          # eliminou post fake
    ("atirar", False): PENALIDADE_ACUSACAO_INJUSTA,  # acusou post real
    ("chao", False): 0,                              # real no chão: sem penalidade
    ("chao", True): 0,                               # fake no chão: só perde vida
}

# Ações que custam 1 vida: coletar um post fake ou deixar um fake chegar
# ao chão. Todo o resto é seguro para as vidas.
ACOES_QUE_PERDEM_VIDA = {("coletar", True), ("chao", True)}


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def pontos_por_acao(acao, eh_fake):
    """Devolve a variação de pontos de uma ação sobre um post.

    acao é "coletar", "atirar" ou "chao". Ação desconhecida levanta
    ValueError.
    """
    chave = (acao, bool(eh_fake))
    if chave not in REGRAS_PONTOS:
        raise ValueError(f"Ação desconhecida: {acao!r}")
    return REGRAS_PONTOS[chave]


def perde_vida(acao, eh_fake):
    """Diz se a ação faz o jogador perder 1 vida (True) ou não (False)."""
    return (acao, bool(eh_fake)) in ACOES_QUE_PERDEM_VIDA