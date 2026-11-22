# TEMP: substituído por src/posts.py e src/funcoes.py do Filipe na integração.
import random

import pygame

from src.config import LARGURA_POST, ALTURA_POST

# Lista fixa de posts usada apenas enquanto a parte do Filipe não está pronta.
POSTS_TEMP = [
    {"texto": "Vacina causa autismo, diz estudo", "fake": True, "pista": "sem fonte confiável"},
    {"texto": "Prefeitura abre vagas de emprego", "fake": False, "pista": "fonte oficial confiável"},
    {"texto": "Político é clonado por IA, diz boato", "fake": True, "pista": "mãos com 6 dedos"},
    {"texto": "Chuva forte prevista pro fim de semana", "fake": False, "pista": "fonte confiável"},
]


def criar_post(largura_tela):
    """Sorteia um post da lista temporária e devolve com rect posicionado acima da tela."""
    base = random.choice(POSTS_TEMP)
    x = random.randint(0, max(0, largura_tela - LARGURA_POST))
    rect = pygame.Rect(x, -ALTURA_POST, LARGURA_POST, ALTURA_POST)
    return {"texto": base["texto"], "fake": base["fake"], "pista": base["pista"], "rect": rect}


def mover_posts(posts, velocidade):
    """Desce todos os posts da lista, alterando o y do rect de cada um."""
    for post in posts:
        post["rect"].y += velocidade


def separar_posts_no_chao(posts, altura_tela):
    """Separa os posts ainda na tela dos que já passaram do fundo da tela."""
    restantes = []
    no_chao = []
    for post in posts:
        if post["rect"].y >= altura_tela:
            no_chao.append(post)
        else:
            restantes.append(post)
    return restantes, no_chao


def pontos_por_acao(acao, eh_fake):
    """Calcula os pontos ganhos (ou perdidos) por uma ação sobre um post real ou fake."""
    if acao == "coletar":
        return 0 if eh_fake else 10
    if acao == "atirar":
        return 15 if eh_fake else -10
    return 0


def perde_vida(acao, eh_fake):
    """Indica se a ação sobre o post (fake ou não) custa uma vida ao jogador."""
    return eh_fake and acao in ("coletar", "chao")
