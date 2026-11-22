import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    FUNDO_ESCURO,
    COR_JOGADOR,
    VIDAS_INICIAIS,
    LARGURA_JOGADOR,
    ALTURA_JOGADOR,
    VELOCIDADE_JOGADOR,
    CAMINHO_RECORDE,
)
from src.dados import salvar_recorde, carregar_recorde
from src.logica_jogo import mover_jogador


def criar_estado():
    """Cria o dicionário de estado inicial de uma partida."""
    jogador_rect = pygame.Rect(
        LARGURA_TELA // 2 - LARGURA_JOGADOR // 2,
        ALTURA_TELA - ALTURA_JOGADOR - 20,
        LARGURA_JOGADOR,
        ALTURA_JOGADOR,
    )
    return {
        "jogador": {"rect": jogador_rect},
        "posts": [],
        "selos": [],
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
        "recorde": carregar_recorde(CAMINHO_RECORDE),
        "estado": "jogando",
        "lupa_ativa": False,
        "tempo_ultimo_post": pygame.time.get_ticks(),
        "tempo_ultimo_disparo": 0,
    }


def tratar_eventos(estado):
    """Processa eventos da janela e do teclado; retorna False se o jogo deve encerrar."""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return False
            if evento.key == pygame.K_r and estado["estado"] == "fim":
                estado.clear()
                estado.update(criar_estado())
    return True


def atualizar_jogador(estado):
    """Move o Lupa-bot para os lados conforme as teclas pressionadas."""
    teclas = pygame.key.get_pressed()
    direcao = 0
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        direcao -= 1
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        direcao += 1

    rect = estado["jogador"]["rect"]
    rect.x = mover_jogador(rect.x, direcao, VELOCIDADE_JOGADOR, LARGURA_TELA, rect.width)


def atualizar(estado):
    """Atualiza a lógica do jogo quando a partida está em andamento."""
    if estado["estado"] != "jogando":
        return
    atualizar_jogador(estado)


def atualizar_titulo_janela(estado):
    """Atualiza o título da janela com pontos, vidas e recorde."""
    pygame.display.set_caption(
        f"{TITULO_JOGO} | Pontos: {estado['pontos']} | "
        f"Vidas: {estado['vidas']} | Recorde: {estado['recorde']}"
    )


def desenhar(tela, estado, fontes):
    """Desenha toda a cena do jogo na tela."""
    tela.fill(FUNDO_ESCURO)
    pygame.draw.rect(tela, COR_JOGADOR, estado["jogador"]["rect"])
    pygame.display.flip()


def executar_jogo():
    """Inicializa o Pygame e executa o loop principal do jogo."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    fontes = {}

    estado = criar_estado()
    rodando = True
    while rodando:
        relogio.tick(FPS)
        rodando = tratar_eventos(estado)
        atualizar(estado)
        atualizar_titulo_janela(estado)
        desenhar(tela, estado, fontes)

    pygame.quit()
