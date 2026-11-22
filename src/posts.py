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