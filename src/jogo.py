import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    FUNDO_ESCURO,
    COR_JOGADOR,
    COR_POST,
    COR_BORDA_POST,
    COR_SELO,
    VIDAS_INICIAIS,
    LARGURA_JOGADOR,
    ALTURA_JOGADOR,
    LARGURA_SELO,
    ALTURA_SELO,
    VELOCIDADE_JOGADOR,
    VELOCIDADE_POSTS,
    VELOCIDADE_SELO,
    INTERVALO_NOVO_POST,
    INTERVALO_DISPARO,
    CAMINHO_RECORDE,
)
from src.dados import salvar_recorde, carregar_recorde
from src.logica_jogo import mover_jogador
from src.temp_integracao import criar_post, mover_posts, separar_posts_no_chao


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
        "tempo_ultimo_disparo": -INTERVALO_DISPARO,
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


def atualizar_posts(estado):
    """Cria novos posts periodicamente, desce os existentes e remove os que chegam ao chão."""
    agora = pygame.time.get_ticks()
    if agora - estado["tempo_ultimo_post"] >= INTERVALO_NOVO_POST:
        estado["posts"].append(criar_post(LARGURA_TELA))
        estado["tempo_ultimo_post"] = agora

    mover_posts(estado["posts"], VELOCIDADE_POSTS)

    restantes, no_chao = separar_posts_no_chao(estado["posts"], ALTURA_TELA)
    estado["posts"] = restantes
    for post in no_chao:
        pass  # TODO: aplicar a acao "chao" quando a pontuacao for integrada


def atualizar_disparo(estado):
    """Dispara um Selo FAKE com Espaço, respeitando o intervalo mínimo entre tiros."""
    teclas = pygame.key.get_pressed()
    agora = pygame.time.get_ticks()
    if teclas[pygame.K_SPACE] and agora - estado["tempo_ultimo_disparo"] >= INTERVALO_DISPARO:
        jogador_rect = estado["jogador"]["rect"]
        selo = pygame.Rect(
            jogador_rect.centerx - LARGURA_SELO // 2,
            jogador_rect.top - ALTURA_SELO,
            LARGURA_SELO,
            ALTURA_SELO,
        )
        estado["selos"].append(selo)
        estado["tempo_ultimo_disparo"] = agora


def atualizar_selos(estado):
    """Sobe os selos disparados e remove os que saem pelo topo da tela."""
    for selo in estado["selos"]:
        selo.y -= VELOCIDADE_SELO
    estado["selos"] = [selo for selo in estado["selos"] if selo.bottom > 0]


def atualizar(estado):
    """Atualiza a lógica do jogo quando a partida está em andamento."""
    if estado["estado"] != "jogando":
        return
    atualizar_jogador(estado)
    atualizar_posts(estado)
    atualizar_disparo(estado)
    atualizar_selos(estado)


def atualizar_titulo_janela(estado):
    """Atualiza o título da janela com pontos, vidas e recorde."""
    pygame.display.set_caption(
        f"{TITULO_JOGO} | Pontos: {estado['pontos']} | "
        f"Vidas: {estado['vidas']} | Recorde: {estado['recorde']}"
    )


def desenhar_post(tela, post):
    """Desenha o cartão de um post como um retângulo simples."""
    pygame.draw.rect(tela, COR_POST, post["rect"])
    pygame.draw.rect(tela, COR_BORDA_POST, post["rect"], 2)


def desenhar(tela, estado, fontes):
    """Desenha toda a cena do jogo na tela."""
    tela.fill(FUNDO_ESCURO)
    pygame.draw.rect(tela, COR_JOGADOR, estado["jogador"]["rect"])
    for post in estado["posts"]:
        desenhar_post(tela, post)
    for selo in estado["selos"]:
        pygame.draw.rect(tela, COR_SELO, selo)
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
