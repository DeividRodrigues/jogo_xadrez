# 🏁 Desafio Avançado: Movimentando as Peças do Xadrez

Este projeto implementa uma simulação avançada de movimentos de peças de xadrez em C, demonstrando técnicas avançadas de programação: **recursividade** e **loops complexos**.

## 🎯 Objetivo

Criar um programa em C que simule o movimento de quatro peças de xadrez usando técnicas avançadas:
- **Torre**: Recursividade para movimento horizontal
- **Bispo**: Recursividade + Loops Aninhados para movimento diagonal
- **Rainha**: Recursividade para movimento em todas as direções
- **Cavalo**: Loops Complexos Aninhados para movimento em "L"

## 📋 Requisitos Atendidos

### ✅ Recursividade
- **Torre**: Função recursiva (5 casas para a direita)
- **Bispo**: Função recursiva (5 casas na diagonal)
- **Rainha**: Função recursiva (8 casas para a esquerda)

### ✅ Loops Complexos
- **Cavalo**: Loops aninhados com múltiplas condições (movimento em "L")
- **Bispo**: Loops aninhados (externo: vertical, interno: horizontal)

### ✅ Técnicas Avançadas
- ✅ Funções recursivas com condições de parada
- ✅ Loops aninhados com múltiplas variáveis
- ✅ Controle de fluxo (continue, break)
- ✅ Comentários detalhados explicando cada técnica
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
  SIMULACAO AVANCADA DE MOVIMENTOS DE    
              XADREZ                     
========================================

PEÇA: TORRE (RECURSIVIDADE)
Movimento: 5 casas para a DIREITA
Técnica: Função Recursiva
Direção do movimento:
------------------------
Casa 1: Direita
Casa 2: Direita
Casa 3: Direita
Casa 4: Direita
Casa 5: Direita

PEÇA: BISPO (RECURSIVIDADE)
Movimento: 5 casas na DIAGONAL (cima e direita)
Técnica: Função Recursiva
Direção do movimento:
------------------------
Casa 1: Cima, Direita
Casa 2: Cima, Direita
Casa 3: Cima, Direita
Casa 4: Cima, Direita
Casa 5: Cima, Direita

PEÇA: RAINHA (RECURSIVIDADE)
Movimento: 8 casas para a ESQUERDA
Técnica: Função Recursiva
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

PEÇA: CAVALO (LOOPS COMPLEXOS ANINHADOS)
Movimento: 3 movimentos em 'L' (cima e direita)
Técnica: Loops Aninhados com Múltiplas Condições
Direção do movimento:
------------------------
Casa 1: Cima
Casa 2: Cima
Casa 3: Direita
Casa 4: Cima
Casa 5: Cima
Casa 6: Direita
Casa 7: Cima
Casa 8: Cima
Casa 9: Direita

PEÇA: BISPO (LOOPS ANINHADOS)
Movimento: 5 casas na DIAGONAL usando loops aninhados
Técnica: Loops Aninhados (externo: vertical, interno: horizontal)
Direção do movimento:
------------------------
Casa 1: Cima, Direita
Casa 2: Cima, Direita
Casa 3: Cima, Direita
Casa 4: Cima, Direita
Casa 5: Cima, Direita

========================================
        RESUMO DAS TÉCNICAS USADAS      
========================================
Torre:   RECURSIVIDADE (5 casas direita)
Bispo:   RECURSIVIDADE + LOOPS ANINHADOS
Rainha:  RECURSIVIDADE (8 casas esquerda)
Cavalo:  LOOPS COMPLEXOS ANINHADOS
========================================

Simulacao avancada concluida com sucesso!
Todas as tecnicas de programacao foram demonstradas.
```

## 🧩 Estrutura do Código

### Torre (Recursividade)
```c
void mover_torre_recursivo(int casas_restantes) {
    if (casas_restantes <= 0) return;
    printf("Casa %d: Direita\n", (CASAS_TORRE - casas_restantes + 1));
    mover_torre_recursivo(casas_restantes - 1);
}
```

### Bispo (Recursividade)
```c
void mover_bispo_recursivo(int casas_restantes) {
    if (casas_restantes <= 0) return;
    printf("Casa %d: Cima, Direita\n", (CASAS_BISPO - casas_restantes + 1));
    mover_bispo_recursivo(casas_restantes - 1);
}
```

### Rainha (Recursividade)
```c
void mover_rainha_recursivo(int casas_restantes) {
    if (casas_restantes <= 0) return;
    printf("Casa %d: Esquerda\n", (CASAS_RAINHA - casas_restantes + 1));
    mover_rainha_recursivo(casas_restantes - 1);
}
```

### Cavalo (Loops Complexos Aninhados)
```c
void mover_cavalo_loops_complexos() {
    for (movimento = 1; movimento <= CASAS_CAVALO; movimento++) {
        for (direcao_vertical = 1; direcao_vertical <= 2; direcao_vertical++) {
            if (direcao_vertical == 1) {
                printf("Casa %d: Cima\n", casa_atual);
            } else {
                printf("Casa %d: Cima\n", casa_atual);
                for (direcao_horizontal = 1; direcao_horizontal <= 1; direcao_horizontal++) {
                    printf("Casa %d: Direita\n", casa_atual);
                    break;
                }
            }
        }
    }
}
```

### Bispo (Loops Aninhados)
```c
void mover_bispo_loops_aninhados() {
    for (movimento_vertical = 1; movimento_vertical <= CASAS_BISPO; movimento_vertical++) {
        for (movimento_horizontal = 1; movimento_horizontal <= 1; movimento_horizontal++) {
            printf("Casa %d: Cima, Direita\n", casa_atual);
            break;
        }
    }
}
```

## 📁 Arquivos do Projeto

- `xadrez.c` - Código fonte principal com técnicas avançadas
- `README.md` - Esta documentação
- `README_C.md` - Documentação técnica detalhada

## 🎓 Técnicas Demonstradas

### 1. Recursividade
- **Condições de Parada**: Evita stack overflow
- **Chamadas Recursivas**: Função chama a si mesma
- **Parâmetros Decrescentes**: Controle da profundidade

### 2. Loops Complexos Aninhados
- **Múltiplas Variáveis**: Controle independente de cada loop
- **Condições Aninhadas**: if/else dentro de loops
- **Controle de Fluxo**: continue e break

### 3. Loops Aninhados
- **Loop Externo**: Controle do movimento vertical
- **Loop Interno**: Controle do movimento horizontal
- **Combinação**: Movimento diagonal

## ✅ Requisitos Não Funcionais

- ✅ **Performance**: Código eficiente sem atrasos
- ✅ **Documentação**: Comentários detalhados explicando cada técnica
- ✅ **Legibilidade**: Código claro e organizado
- ✅ **Variáveis**: Apenas tipos inteiros utilizados
- ✅ **Recursividade Segura**: Condições de parada para evitar stack overflow

## 🏆 Resultado

O programa demonstra com sucesso:
- **Recursividade** para Torre, Bispo e Rainha
- **Loops Complexos Aninhados** para o Cavalo
- **Loops Aninhados** para o Bispo
- **Controle de Fluxo** com continue e break
- **Documentação Completa** de todas as técnicas

Este projeto atende completamente aos requisitos do desafio avançado, demonstrando compreensão e aplicação prática de técnicas avançadas de programação em C.

## 🔗 Link do Repositório

**https://github.com/DeividRodrigues/jogo_xadrez**

O repositório contém o código em C com todas as técnicas avançadas implementadas conforme especificado no desafio.