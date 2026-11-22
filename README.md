# Fato ou Fake?

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Anna Luisa Alexandre Rodrigues
- Filipe Santana Linhares Frota da Mota
- Raissa Marcele Oliveira Machado
- Sebastian Augusto Lopes Camargo

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Em um visual retrô de terminal, posts de rede social (notícia, foto, mensagem) caem do topo da tela. O jogador controla o Lupa-bot, um robô que anda para os lados na parte de baixo da tela, e decide o que fazer com cada post: coletar os reais e eliminar os falsos com o Selo FAKE. Segurando Shift, o jogador ativa a Lupa e vê a pista de cada post (ex.: "sem fonte", "urgência exagerada"), que é o único jeito de diferenciar real de falso.

## Objetivo do jogador

Fazer a maior pontuação possível, coletando posts reais e eliminando posts falsos com o Selo FAKE, enquanto mantém as 3 vidas e evita que posts falsos cheguem ao chão ou sejam coletados por engano.

## Regras do jogo

- Encostar num post real com o robô coleta: +10 pontos.
- Atirar o Selo FAKE (Espaço) num post falso elimina: +15 pontos.
- Atirar o Selo FAKE num post real é uma acusação injusta: -10 pontos.
- Coletar um post falso, ou deixar um post falso chegar ao chão, custa 1 vida; post real no chão não tem penalidade.
- O jogador começa com 3 vidas; ao chegar a 0, a partida termina e o recorde é salvo se for batido.

## Controles

- Seta para a esquerda ou **A**: mover o Lupa-bot para a esquerda
- Seta para a direita ou **D**: mover o Lupa-bot para a direita
- **Espaço**: disparar o Selo FAKE
- **Shift** (esquerdo ou direito, segurado): ativar a Lupa e revelar as pistas dos posts
- **R**: jogar de novo, na tela de fim de jogo
- **Esc**: sair do jogo em qualquer momento

## Como executar o projeto

```bash
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
