# 🏁 Jogo de Xadrez em Python

Um jogo de xadrez completo implementado em Python com interface de linha de comando, incluindo todas as regras básicas e movimentação de peças.

## 🎯 Características

- **Tabuleiro completo** com todas as peças de xadrez
- **Movimentação realista** seguindo as regras do xadrez
- **Interface de linha de comando** intuitiva
- **Validação de movimentos** completa
- **Histórico de movimentos** e comandos especiais
- **Símbolos Unicode** para visualização das peças

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Instalação e Execução

1. Clone ou baixe o projeto:
```bash
git clone <url-do-repositorio>
cd desafio_pecas_xadrez
```

2. Execute o jogo:
```bash
python chess_game.py
```

Ou se preferir executar diretamente:
```bash
python3 chess_game.py
```

## 🎮 Como Jogar

### Movimentos
- Digite movimentos no formato: `origem-destino`
- Exemplo: `e2-e4` (move peão de e2 para e4)
- Use coordenadas de xadrez: a-h (colunas), 1-8 (linhas)

### Comandos Especiais
- `help` ou `h` - Exibe ajuda
- `quit` ou `q` - Sai do jogo
- `reset` ou `r` - Reinicia o jogo
- `history` - Mostra histórico de movimentos
- `moves` - Mostra movimentos possíveis

### Peças
- **Brancas**: ♔♕♖♗♘♙
- **Pretas**: ♚♛♜♝♞♟

## 📁 Estrutura do Projeto

```
desafio_pecas_xadrez/
├── chess_pieces.py      # Classes das peças de xadrez
├── chess_board.py       # Classe do tabuleiro e lógica do jogo
├── chess_game.py        # Interface principal e loop do jogo
├── requirements.txt     # Dependências (apenas Python padrão)
└── README.md           # Este arquivo
```

## 🧩 Componentes

### `chess_pieces.py`
Contém todas as classes das peças:
- `Piece` (classe base abstrata)
- `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, `King`

Cada peça implementa:
- `get_possible_moves()` - Calcula movimentos válidos
- `get_symbol()` - Retorna símbolo Unicode da peça
- Validação de posições e capturas

### `chess_board.py`
Gerencia o tabuleiro e lógica do jogo:
- Inicialização das peças
- Validação de movimentos
- Histórico de jogadas
- Detecção de fim de jogo

### `chess_game.py`
Interface principal do jogo:
- Parser de notação de xadrez
- Comandos interativos
- Visualização do tabuleiro
- Loop principal do jogo

## 🎯 Regras Implementadas

### Movimentos Básicos
- **Peão**: Movimento direto, captura diagonal, movimento duplo inicial
- **Torre**: Movimento horizontal e vertical ilimitado
- **Cavalo**: Movimento em L (2+1 casas)
- **Bispo**: Movimento diagonal ilimitado
- **Rainha**: Combinação de torre e bispo
- **Rei**: Movimento de uma casa em qualquer direção

### Validações
- ✅ Verificação de limites do tabuleiro
- ✅ Prevenção de captura de peças próprias
- ✅ Verificação de bloqueios no caminho
- ✅ Alternância correta de jogadores

## 🔧 Personalização

O código é modular e facilmente extensível:

1. **Adicionar novas regras**: Modifique as classes de peças em `chess_pieces.py`
2. **Melhorar interface**: Edite `chess_game.py` para melhor UX
3. **Implementar novas funcionalidades**: Adicione métodos em `chess_board.py`

## 🐛 Limitações Atuais

- Detecção de xeque/xeque-mate simplificada
- Não implementa roque, en passant ou promoção de peões
- Sem detecção de empates por repetição ou posição

## 📝 Exemplos de Uso

```bash
# Iniciar o jogo
python chess_game.py

# Durante o jogo:
Digite seu movimento: e2-e4
✅ Movimento realizado: e2-e4

# Ver ajuda
Digite seu movimento: help

# Ver movimentos possíveis
Digite seu movimento: moves

# Sair do jogo
Digite seu movimento: quit
```

## 🤝 Contribuição

Este é um projeto educacional. Sinta-se livre para:
- Reportar bugs
- Sugerir melhorias
- Implementar novas funcionalidades
- Otimizar o código

## 📄 Licença

Este projeto é de código aberto e pode ser usado livremente para fins educacionais.
