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
