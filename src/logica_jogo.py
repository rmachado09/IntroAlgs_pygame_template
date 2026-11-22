"""Funções puras e testáveis do jogo, separadas da renderização e do Pygame."""
from src.funcoes import limitar_valor


def mover_jogador(x, direcao, velocidade, largura_tela, largura_jogador):
    """Calcula a nova posição x do jogador, mantendo-o dentro da tela."""
    novo_x = x + direcao * velocidade
    return limitar_valor(novo_x, 0, largura_tela - largura_jogador)


def quebrar_texto(texto, max_caracteres):
    """Quebra um texto em linhas de até max_caracteres, sem cortar palavras."""
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        candidata = f"{linha_atual} {palavra}".strip()
        if len(candidata) <= max_caracteres:
            linha_atual = candidata
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)
    return linhas
