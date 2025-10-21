# 🏁 Desafio: Movimentando as Peças do Xadrez

Este projeto implementa uma simulação de movimentos de peças de xadrez em C, demonstrando o uso de diferentes estruturas de repetição.

## 🎯 Objetivo

Criar um programa em C que simule o movimento de três peças de xadrez:
- **Torre**: Move-se em linha reta (horizontal/vertical)
- **Bispo**: Move-se na diagonal
- **Rainha**: Move-se em todas as direções

## 📋 Requisitos Atendidos

### ✅ Estruturas de Repetição
- **Torre**: FOR loop (5 casas para a direita)
- **Bispo**: WHILE loop (5 casas na diagonal)
- **Rainha**: DO-WHILE loop (8 casas para a esquerda)

### ✅ Funcionalidades
- ✅ Entrada de dados definida no código
- ✅ Lógica de movimentação específica para cada peça
- ✅ Saída formatada com printf
- ✅ Comentários explicativos
- ✅ Código organizado e legível

## 🚀 Como Compilar e Executar

### Compilação
```bash
gcc -o xadrez xadrez.c
```

### Execução
```bash
./xadrez
```

## 📊 Saída do Programa

```
========================================
    SIMULACAO DE MOVIMENTOS DE XADREZ   
========================================

PEÇA: TORRE
Movimento: 5 casas para a DIREITA
Estrutura de repetição: FOR
Direção do movimento:
------------------------
Casa 1: Direita
Casa 2: Direita
Casa 3: Direita
Casa 4: Direita
Casa 5: Direita

PEÇA: BISPO
Movimento: 5 casas na DIAGONAL (cima e direita)
Estrutura de repetição: WHILE
Direção do movimento:
------------------------
Casa 1: Cima, Direita
Casa 2: Cima, Direita
Casa 3: Cima, Direita
Casa 4: Cima, Direita
Casa 5: Cima, Direita

PEÇA: RAINHA
Movimento: 8 casas para a ESQUERDA
Estrutura de repetição: DO-WHILE
Direção do movimento:
------------------------
Casa 1: Esquerda
Casa 2: Esquerda
Casa 3: Esquerda
Casa 4: Esquerda
Casa 5: Esquerda
Casa 6: Esquerda
Casa 7: Esquerda
Casa 8: Esquerda

========================================
           RESUMO DOS MOVIMENTOS       
========================================
Torre:   5 casas para a DIREITA (FOR)
Bispo:   5 casas na DIAGONAL (WHILE)
Rainha:  8 casas para a ESQUERDA (DO-WHILE)
========================================

Simulacao concluida com sucesso!
Todas as pecas executaram seus movimentos.
```

## 🧩 Estrutura do Código

### Torre (FOR Loop)
```c
for (i = 1; i <= casas_torre; i++) {
    printf("Casa %d: Direita\n", i);
}
```

### Bispo (WHILE Loop)
```c
contador_bispo = 1;
while (contador_bispo <= casas_bispo) {
    printf("Casa %d: Cima, Direita\n", contador_bispo);
    contador_bispo++;
}
```

### Rainha (DO-WHILE Loop)
```c
contador_rainha = 1;
do {
    printf("Casa %d: Esquerda\n", contador_rainha);
    contador_rainha++;
} while (contador_rainha <= casas_rainha);
```

## 📁 Arquivos do Projeto

- `xadrez.c` - Código fonte principal
- `README.md` - Esta documentação
- `README_C.md` - Documentação técnica detalhada

## 🎓 Conceitos Demonstrados

1. **FOR Loop**: Controle preciso de iterações
2. **WHILE Loop**: Repetição baseada em condição
3. **DO-WHILE Loop**: Execução garantida pelo menos uma vez
4. **Variáveis**: Uso de tipos inteiros
5. **Saída Formatada**: Uso de printf
6. **Comentários**: Documentação do código

## ✅ Requisitos Não Funcionais

- ✅ **Performance**: Código eficiente sem atrasos
- ✅ **Documentação**: Comentários explicativos
- ✅ **Legibilidade**: Código claro e organizado
- ✅ **Variáveis**: Apenas tipos inteiros utilizados

## 🏆 Resultado

O programa demonstra com sucesso:
- Uso correto das três estruturas de repetição
- Simulação realista dos movimentos das peças
- Saída formatada e clara
- Código bem documentado e organizado

Este projeto atende completamente aos requisitos do desafio de nível novato, demonstrando compreensão e aplicação prática das estruturas de repetição em C.

## 🔗 Link do Repositório

**https://github.com/DeividRodrigues/jogo_xadrez**

O repositório contém apenas o código em C conforme especificado no desafio.