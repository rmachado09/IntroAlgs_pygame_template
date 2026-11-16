# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> Fato ou Fake?

## 2. Integrantes do grupo

- Nome 1: Anna Luisa Alexandre Rodrigues
- Nome 2: Filipe Santana Linhares Frota da Mota
- Nome 3: Raissa Marcele Oliveira Machado
- Nome 4: Sebastian Augusto Lopes Camargo

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> Conteúdos reais e artificiais: reconhecer sinais de textos, imagens e notícias manipulados ou gerados por IA, e a importância de conferir antes de compartilhar.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> O jogador é um robô antifake que protege um feed de redes sociais. Posts reais e posts falsos (gerados ou manipulados por IA) caem ao mesmo tempo, e o jogador precisa distingui-los. Os falsos trazem pistas sutis, como fonte ausente, urgência exagerada e imagem com defeitos, que podem ser vistas com a Lupa. Deixar um falso passar ou acusar um post real por engano tem consequências, então o tema define as regras, a pontuação e os desafios, e não só o cenário.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Arcade de ação com perguntas e decisões: desviar, coletar e atirar em itens que caem, no estilo "invasores", com ondas de dificuldade crescente

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> Em um visual retrô de terminal e pixel art, o feed cai do topo da tela em forma de cartões de posts (notícia, foto, mensagem). O jogador controla o Lupa-bot na parte de baixo, movendo-se para os lados. Posts reais devem ser coletados encostando neles, e posts falsos devem ser eliminados com o Selo FAKE. Segurando a Lupa, o jogador vê as pistas de cada post, mas gasta uma energia limitada que recarrega devagar, o que o obriga a escolher quando conferir. Ao fim de cada onda, aparece um Relatório de Checagem com dicas reais de como identificar conteúdo falso. Os desafios são a velocidade crescente, o gerenciamento da energia da Lupa e o risco de acusar um post real.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Limpar o feed sobrevivendo a 5 ondas de posts, coletando o máximo de informações reais e eliminando as falsas, para fazer a maior pontuação possível e bater o recorde.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

Regra 1: Posts reais caem e dão +10 pontos ao serem coletados; posts falsos eliminados com o Selo FAKE dão +15.
Regra 2: O jogador tem 3 vidas e perde 1 ao coletar um post falso ou ao deixar um post falso chegar ao chão.
Regra 3: Atirar o Selo FAKE em um post real (acusação injusta) tira 10 pontos e zera o combo.
Regra 4: A Lupa (segurar Shift) revela as pistas dos posts, consome energia e recarrega sozinha com o tempo.
Regra 5: A cada 10 posts começa uma nova onda, mais rápida e com pistas mais difíceis, e acertos seguidos formam um combo que multiplica os pontos.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> Concluir as 5 ondas (50 posts) com pelo menos 1 vida. Aparece a mensagem "Feed limpo!" com a pontuação final e o recorde.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> A partida termina em derrota quando as 3 vidas acabam ("O feed foi invadido por fakes"). Em qualquer fim de partida, a tela final mostra a pontuação, o recorde e a opção de jogar de novo ou sair.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** o Lupa-bot, um robô com lupa que se move na parte de baixo da tela e dispara o Selo FAKE.
- **Obstáculos ou desafios:** posts falsos com efeito de glitch, queda cada vez mais rápida, ondas com pistas mais sutis e energia limitada da Lupa.
- **Itens ou objetos de interação (se houver):** posts reais (para coletar), posts falsos (para eliminar), Selo FAKE (projétil) e a Lupa, que revela as pistas.
- **Pontuação, vidas, tempo ou progresso:** pontuação, 3 vidas em forma de corações, barra de energia da Lupa, combo e indicador de onda (ex.: onda 2/5), mais o Relatório de Checagem ao fim de cada onda.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> Setas esquerda e direita (ou A e D) para mover o robô; Espaço para disparar o Selo FAKE; Shift segurado para usar a Lupa; Enter para avançar telas; P para pausar; Esc para sair

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Tratar colisões e disparos no Pygame e controlar vários posts caindo ao mesmo tempo.
- Dificuldade 2: Equilibrar velocidade, energia da Lupa e pontuação, e criar posts com pistas justas, nem óbvias demais nem impossíveis.
- Dificuldade 3: Organizar o trabalho em grupo no GitHub e testar a lógica separada da interface.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> Uma tela de jogo em que o Lupa-bot se move e dispara o Selo FAKE; posts reais e falsos caindo, lidos de um arquivo com pelo menos 20 posts; Lupa funcionando com energia; pontuação, 3 vidas e combo; pelo menos 3 ondas com dificuldade crescente; condições de vitória e derrota; recorde salvo em arquivo; código organizado em funções, README preenchido e testes simples da lógica (pontuação, vidas e fim de partida).

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: Chefão na última onda, o "Deepfake Gigante", que muda de rosto e precisa ser analisado com a Lupa antes de ser derrotado.
- Melhoria 2: Power-ups, como "Fact-check" (revela todas as pistas por alguns segundos) e "Congelar feed".
- Melhoria 3: Menu inicial, ranking dos melhores resultados, efeitos sonoros e animações de glitch.
