"""Testes dos posts do jogo (src/posts.py)."""

import copy
import random

import pygame

from src import posts
from src.posts import (
    ALTURA_POST,
    LARGURA_POST,
    MAX_CARACTERES_PISTA,
    MAX_CARACTERES_TEXTO,
    POSTS_BASE,
    carregar_posts,
    criar_post,
    mover_posts,
    separar_posts_no_chao,
)


def criar_post_com_y(y):
    """Monta um post simples com o rect na altura y (auxiliar dos testes)."""
    return {"texto": "teste", "fake": False, "pista": "teste",
            "rect": pygame.Rect(0, y, LARGURA_POST, ALTURA_POST)}


# --- Conteúdo de POSTS_BASE ---

def test_posts_base_tem_pelo_menos_12_posts():
    """A lista base precisa ter ao menos 12 posts."""
    assert len(POSTS_BASE) >= 12


def test_posts_base_tem_chaves_e_tipos_certos():
    """Todo post base tem texto (str), fake (bool) e pista (str), sem rect."""
    for post in POSTS_BASE:
        assert set(post.keys()) == {"texto", "fake", "pista"}
        assert isinstance(post["texto"], str)
        assert isinstance(post["fake"], bool)
        assert isinstance(post["pista"], str)


def test_posts_base_respeita_limites_de_tamanho():
    """Texto tem até 45 caracteres e pista até 25, e nenhum é vazio."""
    for post in POSTS_BASE:
        assert 0 < len(post["texto"]) <= MAX_CARACTERES_TEXTO
        assert 0 < len(post["pista"]) <= MAX_CARACTERES_PISTA


def test_posts_base_tem_reais_e_falsos_na_mesma_quantidade():
    """Metade dos posts é real e metade é falsa."""
    falsos = [post for post in POSTS_BASE if post["fake"]]
    reais = [post for post in POSTS_BASE if not post["fake"]]
    assert len(falsos) > 0
    assert len(reais) > 0
    assert len(falsos) == len(reais)


def test_posts_base_nao_tem_textos_repetidos():
    """Cada texto aparece uma única vez na lista base."""
    textos = [post["texto"] for post in POSTS_BASE]
    assert len(textos) == len(set(textos))


# --- criar_post ---

def test_criar_post_devolve_rect_dentro_da_largura_e_acima_da_tela():
    """O rect nasce acima da tela e o cartão inteiro cabe na largura."""
    random.seed(42)
    for _ in range(200):
        post = criar_post(800)
        rect = post["rect"]
        assert isinstance(rect, pygame.Rect)
        assert rect.width == LARGURA_POST
        assert rect.height == ALTURA_POST
        assert rect.bottom <= 0          # acima da tela
        assert rect.left >= 0            # não passa da borda esquerda
        assert rect.right <= 800         # não passa da borda direita


def test_criar_post_sorteia_x_entre_0_e_largura_menos_post(monkeypatch):
    """O x sorteado vai de 0 até largura_tela - LARGURA_POST."""
    pedidos = []

    def randint_falso(minimo, maximo):
        pedidos.append((minimo, maximo))
        return maximo

    monkeypatch.setattr(posts.random, "randint", randint_falso)
    post = criar_post(800)
    assert pedidos == [(0, 800 - LARGURA_POST)]
    assert post["rect"].x == 800 - LARGURA_POST
    assert post["rect"].y == -ALTURA_POST


def test_criar_post_usa_random_choice_e_devolve_copia(monkeypatch):
    """O post vem do sorteio de POSTS_BASE, mas é uma cópia, não o original."""
    monkeypatch.setattr(posts.random, "choice", lambda lista: lista[0])
    post = criar_post(800)
    assert post is not POSTS_BASE[0]
    assert post["texto"] == POSTS_BASE[0]["texto"]
    assert post["fake"] == POSTS_BASE[0]["fake"]
    assert post["pista"] == POSTS_BASE[0]["pista"]


def test_criar_post_nao_altera_posts_base():
    """Criar e mexer nos posts que caem não muda a lista base."""
    original = copy.deepcopy(POSTS_BASE)
    random.seed(7)
    for _ in range(50):
        post = criar_post(800)
        post["texto"] = "alterado"
        post["fake"] = not post["fake"]
        post["rect"].y += 500
    assert POSTS_BASE == original
    assert all("rect" not in post for post in POSTS_BASE)


def test_criar_post_com_seed_e_deterministico():
    """Com a mesma semente, o sorteio repete o mesmo post e a mesma posição."""
    random.seed(123)
    primeiro = criar_post(800)
    random.seed(123)
    segundo = criar_post(800)
    assert primeiro == segundo


# --- mover_posts ---

def test_mover_posts_desce_os_posts_pela_velocidade():
    """Cada post desce exatamente a velocidade informada."""
    lista = [criar_post_com_y(-60), criar_post_com_y(100)]
    mover_posts(lista, 5)
    assert lista[0]["rect"].y == -55
    assert lista[1]["rect"].y == 105


def test_mover_posts_soma_a_cada_chamada():
    """Chamar duas vezes desce duas vezes a velocidade."""
    lista = [criar_post_com_y(0)]
    mover_posts(lista, 3)
    mover_posts(lista, 3)
    assert lista[0]["rect"].y == 6


def test_mover_posts_aceita_lista_vazia():
    """Lista vazia não gera erro e continua vazia."""
    lista = []
    mover_posts(lista, 5)
    assert lista == []


# --- separar_posts_no_chao ---

def test_separar_posts_no_chao_separa_post_na_tela_e_post_no_chao():
    """Um post na tela fica em restantes e um no chão vai para no_chao."""
    na_tela = criar_post_com_y(100)
    no_chao_post = criar_post_com_y(600)
    restantes, no_chao = separar_posts_no_chao([na_tela, no_chao_post], 600)
    assert restantes == [na_tela]
    assert no_chao == [no_chao_post]


def test_separar_posts_no_chao_considera_a_borda():
    """top == altura_tela já é chão; top logo acima ainda está caindo."""
    quase = criar_post_com_y(599)
    limite = criar_post_com_y(600)
    restantes, no_chao = separar_posts_no_chao([quase, limite], 600)
    assert restantes == [quase]
    assert no_chao == [limite]


def test_separar_posts_no_chao_devolve_listas_novas():
    """A lista original não é alterada e as duas devolvidas são novas."""
    original = [criar_post_com_y(100), criar_post_com_y(700)]
    copia = list(original)
    restantes, no_chao = separar_posts_no_chao(original, 600)
    assert original == copia
    assert restantes is not original
    assert no_chao is not original


def test_separar_posts_no_chao_com_lista_vazia():
    """Sem posts, as duas listas devolvidas ficam vazias."""
    assert separar_posts_no_chao([], 600) == ([], [])


# --- carregar_posts (opcional) ---

def test_carregar_posts_sem_arquivo_devolve_posts_base(tmp_path):
    """Se o arquivo não existe, usa os posts da lista base."""
    assert carregar_posts(tmp_path / "nao_existe.txt") == POSTS_BASE


def test_carregar_posts_le_arquivo_e_ignora_linhas_invalidas(tmp_path):
    """Lê texto;fake;pista, ignorando comentários, vazias e mal formadas."""
    arquivo = tmp_path / "posts.txt"
    arquivo.write_text(
        "# comentário\n"
        "Notícia com fonte;false;fonte: site oficial\n"
        "\n"
        "Promessa absurda;TRUE;promessa boa demais\n"
        "linha sem separadores\n"
        "Fake com valor ruim;talvez;sem pista\n",
        encoding="utf-8",
    )
    assert carregar_posts(arquivo) == [
        {"texto": "Notícia com fonte", "fake": False,
         "pista": "fonte: site oficial"},
        {"texto": "Promessa absurda", "fake": True,
         "pista": "promessa boa demais"},
    ]


def test_carregar_posts_arquivo_sem_posts_validos_usa_posts_base(tmp_path):
    """Arquivo sem nenhuma linha válida cai de volta na lista base."""
    arquivo = tmp_path / "posts.txt"
    arquivo.write_text("# só comentário\n", encoding="utf-8")
    assert carregar_posts(arquivo) == POSTS_BASE
