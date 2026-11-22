import random

import jogo


# Tamanho do cartão de cada post, em pixels.
LARGURA_POST = 220
ALTURA_POST = 60

# Texto cabe em 2 linhas de um cartão de 220 px; a pista é só uma dica curta.
MAX_CARACTERES_TEXTO = 45
MAX_CARACTERES_PISTA = 25

# Cada post tem o texto que aparece no cartão, se é fake e a pista que a
# Lupa revela. Sem a Lupa, reais e falsos têm a mesma aparência: é a pista
# que permite decidir. Falsos trazem sinais de conteúdo gerado ou manipulado
# por IA (ou de desinformação); reais trazem sinais de que são confiáveis.


POSTS_BASE = [
    # --- Posts reais (fake = False) ---
    {"texto": "Escola divulga calendário de provas",
     "fake": False, "pista": "fonte: site da escola"},
    {"texto": "Vacina nova aprovada após testes",
     "fake": False, "pista": "fonte: órgão oficial"},
    {"texto": "Previsão: chuva forte à tarde na região",
     "fake": False, "pista": "várias agências confirmam"},
    {"texto": "Ônibus da linha 12 terá horário extra",
     "fake": False, "pista": "aviso oficial no terminal"},
    {"texto": "Foto: biblioteca da escola reaberta",
     "fake": False, "pista": "data e local claros"},
    {"texto": "Mensagem do posto: aberto das 8h às 19h",
     "fake": False, "pista": "remetente identificado"},
    {"texto": "Áudio: recado da coordenação à turma",
     "fake": False, "pista": "canal oficial da escola"},
    {"texto": "Dormir bem ajuda a aprender, diz estudo",
     "fake": False, "pista": "autores e revista citados"},
    {"texto": "Anúncio: feira de ciências gratuita",
     "fake": False, "pista": "organizador identificado"},
    {"texto": "Celulares recebem atualização de segurança",
     "fake": False, "pista": "nota no site oficial"},

    # --- Posts falsos (fake = True) ---
    {"texto": "URGENTE: compartilhe antes que apaguem!",
     "fake": True, "pista": "urgência exagerada"},
    {"texto": "Foto: prefeito inaugura praça nova",
     "fake": True, "pista": "mãos com 6 dedos"},
    {"texto": "Foto da enchente no centro da cidade",
     "fake": True, "pista": "texto borrado na foto"},
    {"texto": "Áudio: diretora cancela todas as aulas",
     "fake": True, "pista": "voz robótica"},
    {"texto": "Ganhe um celular novo clicando aqui",
     "fake": True, "pista": "link encurtado estranho"},
    {"texto": "Chá milagroso cura qualquer doença",
     "fake": True, "pista": "promessa boa demais"},
    {"texto": "Repasse a 10 contatos e ganhe crédito",
     "fake": True, "pista": "corrente sem fonte"},
    {"texto": "Notícia: feriado novo em 31 de fevereiro",
     "fake": True, "pista": "data inexistente"},
    {"texto": "Metade da cidade ficará sem luz amanhã",
     "fake": True, "pista": "sem fonte"},
    {"texto": "Vídeo: diretor anuncia fim das provas",
     "fake": True, "pista": "boca fora de sincronia"},
]


def criar_post(largura_tela):
    """Sorteia um post de POSTS_BASE e devolve uma cópia pronta para cair."""
    base = random.choice(POSTS_BASE)

    # dict(base) é uma cópia: os valores são str e bool (imutáveis), então
    # mexer no post que cai nunca altera o POSTS_BASE.
    post = dict(base)

    # O post nasce logo acima da tela (y negativo) e cai a partir dali.
    # O x sorteado garante que o cartão inteiro fique dentro da largura.
    x_maximo = max(0, largura_tela - LARGURA_POST)
    x = random.randint(0, x_maximo)
    post["rect"] = pygame.Rect(x, -ALTURA_POST, LARGURA_POST, ALTURA_POST)
    return post


def mover_posts(posts, velocidade):
    """Desce todos os posts da lista, somando a velocidade ao rect.y.

    Use velocidade inteira (pixels por quadro): o pygame.Rect guarda
    coordenadas inteiras e descartaria a parte decimal.
    """
    for post in posts:
        post["rect"].y += velocidade


def separar_posts_no_chao(posts, altura_tela):
    """Separa os posts que chegaram ao chão dos que ainda estão caindo.

    Devolve (restantes, no_chao), duas listas novas. Um post está no chão
    quando o topo do cartão alcança a altura da tela (rect.top >= altura).
    """
    restantes = []
    no_chao = []
    for post in posts:
        if post["rect"].top >= altura_tela:
            no_chao.append(post)
        else:
            restantes.append(post)
    return restantes, no_chao


def carregar_posts(caminho):
    """Lê os posts de um arquivo de texto; sem arquivo, usa POSTS_BASE.

    Formato: uma linha por post, "texto;fake;pista", com fake escrito como
    "true" ou "false". Linhas em branco, começando com "#" ou mal formadas
    são ignoradas. Se o arquivo não existir ou não tiver nenhum post
    válido, devolve POSTS_BASE.
    """
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            linhas = arquivo.read().splitlines()
    except FileNotFoundError:
        
        return POSTS_BASE