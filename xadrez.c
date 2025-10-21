/*
 * DESAFIO AVANÇADO: Movimentando as Peças do Xadrez
 * ==================================================
 * 
 * Este programa simula o movimento de quatro peças de xadrez usando
 * técnicas avançadas de programação:
 * 
 * - Torre: Recursividade para movimento horizontal
 * - Bispo: Recursividade + Loops Aninhados para movimento diagonal
 * - Rainha: Recursividade para movimento em todas as direções
 * - Cavalo: Loops Complexos Aninhados para movimento em "L"
 * 
 * Técnicas implementadas:
 * - Recursividade (Torre, Bispo, Rainha)
 * - Loops Aninhados (Bispo, Cavalo)
 * - Loops Complexos (Cavalo com múltiplas condições)
 * - Controle de fluxo (continue, break)
 * 
 * Autor: Deivid Rodrigues
 * Data: 2025
 */

#include <stdio.h>
#include <stdlib.h>

// Constantes para controle dos movimentos
#define CASAS_TORRE 5
#define CASAS_BISPO 5
#define CASAS_RAINHA 8
#define CASAS_CAVALO 3

// Protótipos das funções recursivas
void mover_torre_recursivo(int casas_restantes);
void mover_bispo_recursivo(int casas_restantes);
void mover_rainha_recursivo(int casas_restantes);

// Protótipos das funções com loops complexos
void mover_cavalo_loops_complexos();
void mover_bispo_loops_aninhados();

int main() {
    printf("========================================\n");
    printf("  SIMULACAO AVANCADA DE MOVIMENTOS DE    \n");
    printf("              XADREZ                     \n");
    printf("========================================\n\n");
    
    /*
     * TORRE - Movimento usando RECURSIVIDADE
     * Move-se em linha reta para a direita
     */
    printf("PEÇA: TORRE (RECURSIVIDADE)\n");
    printf("Movimento: %d casas para a DIREITA\n", CASAS_TORRE);
    printf("Técnica: Função Recursiva\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    mover_torre_recursivo(CASAS_TORRE);
    printf("\n");
    
    /*
     * BISPO - Movimento usando RECURSIVIDADE
     * Move-se na diagonal (cima e direita)
     */
    printf("PEÇA: BISPO (RECURSIVIDADE)\n");
    printf("Movimento: %d casas na DIAGONAL (cima e direita)\n", CASAS_BISPO);
    printf("Técnica: Função Recursiva\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    mover_bispo_recursivo(CASAS_BISPO);
    printf("\n");
    
    /*
     * RAINHA - Movimento usando RECURSIVIDADE
     * Move-se para a esquerda
     */
    printf("PEÇA: RAINHA (RECURSIVIDADE)\n");
    printf("Movimento: %d casas para a ESQUERDA\n", CASAS_RAINHA);
    printf("Técnica: Função Recursiva\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    mover_rainha_recursivo(CASAS_RAINHA);
    printf("\n");
    
    /*
     * CAVALO - Movimento usando LOOPS COMPLEXOS ANINHADOS
     * Move-se em "L" (duas casas para cima e uma para a direita)
     */
    printf("PEÇA: CAVALO (LOOPS COMPLEXOS ANINHADOS)\n");
    printf("Movimento: %d movimentos em 'L' (cima e direita)\n", CASAS_CAVALO);
    printf("Técnica: Loops Aninhados com Múltiplas Condições\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    mover_cavalo_loops_complexos();
    printf("\n");
    
    /*
     * BISPO - Movimento usando LOOPS ANINHADOS
     * Demonstra loops aninhados para movimento diagonal
     */
    printf("PEÇA: BISPO (LOOPS ANINHADOS)\n");
    printf("Movimento: %d casas na DIAGONAL usando loops aninhados\n", CASAS_BISPO);
    printf("Técnica: Loops Aninhados (externo: vertical, interno: horizontal)\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    mover_bispo_loops_aninhados();
    printf("\n");
    
    /*
     * RESUMO DAS TÉCNICAS IMPLEMENTADAS
     */
    printf("========================================\n");
    printf("        RESUMO DAS TÉCNICAS USADAS      \n");
    printf("========================================\n");
    printf("Torre:   RECURSIVIDADE (%d casas direita)\n", CASAS_TORRE);
    printf("Bispo:   RECURSIVIDADE + LOOPS ANINHADOS\n");
    printf("Rainha:  RECURSIVIDADE (%d casas esquerda)\n", CASAS_RAINHA);
    printf("Cavalo:  LOOPS COMPLEXOS ANINHADOS\n");
    printf("========================================\n");
    
    printf("\nSimulacao avancada concluida com sucesso!\n");
    printf("Todas as tecnicas de programacao foram demonstradas.\n");
    
    return 0;
}

/*
 * FUNÇÃO RECURSIVA: Torre
 * Simula movimento da Torre usando recursividade
 * Move-se para a direita até completar todas as casas
 */
void mover_torre_recursivo(int casas_restantes) {
    // Condição de parada da recursão
    if (casas_restantes <= 0) {
        return;
    }
    
    // Imprime a direção do movimento
    printf("Casa %d: Direita\n", (CASAS_TORRE - casas_restantes + 1));
    
    // Chamada recursiva com uma casa a menos
    mover_torre_recursivo(casas_restantes - 1);
}

/*
 * FUNÇÃO RECURSIVA: Bispo
 * Simula movimento do Bispo usando recursividade
 * Move-se na diagonal (cima e direita)
 */
void mover_bispo_recursivo(int casas_restantes) {
    // Condição de parada da recursão
    if (casas_restantes <= 0) {
        return;
    }
    
    // Imprime a direção do movimento diagonal
    printf("Casa %d: Cima, Direita\n", (CASAS_BISPO - casas_restantes + 1));
    
    // Chamada recursiva com uma casa a menos
    mover_bispo_recursivo(casas_restantes - 1);
}

/*
 * FUNÇÃO RECURSIVA: Rainha
 * Simula movimento da Rainha usando recursividade
 * Move-se para a esquerda
 */
void mover_rainha_recursivo(int casas_restantes) {
    // Condição de parada da recursão
    if (casas_restantes <= 0) {
        return;
    }
    
    // Imprime a direção do movimento
    printf("Casa %d: Esquerda\n", (CASAS_RAINHA - casas_restantes + 1));
    
    // Chamada recursiva com uma casa a menos
    mover_rainha_recursivo(casas_restantes - 1);
}

/*
 * FUNÇÃO COM LOOPS COMPLEXOS ANINHADOS: Cavalo
 * Simula movimento do Cavalo em "L" usando loops aninhados
 * com múltiplas variáveis e condições
 */
void mover_cavalo_loops_complexos() {
    int movimento = 1;           // Contador de movimentos
    int direcao_vertical = 0;     // Controle da direção vertical
    int direcao_horizontal = 0;   // Controle da direção horizontal
    int casa_atual = 1;          // Casa atual do movimento
    
    // LOOP EXTERNO: Controla o número total de movimentos
    for (movimento = 1; movimento <= CASAS_CAVALO; movimento++) {
        
        // LOOP INTERNO: Simula o movimento em "L" (2 casas verticais + 1 horizontal)
        for (direcao_vertical = 1; direcao_vertical <= 2; direcao_vertical++) {
            
            // Múltiplas condições para controle preciso do movimento
            if (direcao_vertical == 1) {
                printf("Casa %d: Cima\n", casa_atual);
                casa_atual++;
            } else if (direcao_vertical == 2) {
                printf("Casa %d: Cima\n", casa_atual);
                casa_atual++;
                
                // LOOP ANINHADO ADICIONAL: Movimento horizontal
                for (direcao_horizontal = 1; direcao_horizontal <= 1; direcao_horizontal++) {
                    printf("Casa %d: Direita\n", casa_atual);
                    casa_atual++;
                    
                    // Uso de BREAK para sair do loop interno após 1 movimento horizontal
                    break;
                }
            }
            
            // Uso de CONTINUE para pular para próxima iteração se necessário
            if (direcao_vertical < 2) {
                continue;
            }
        }
    }
}

/*
 * FUNÇÃO COM LOOPS ANINHADOS: Bispo
 * Simula movimento do Bispo usando loops aninhados
 * Loop externo: movimento vertical (cima)
 * Loop interno: movimento horizontal (direita)
 */
void mover_bispo_loops_aninhados() {
    int movimento_vertical = 1;   // Controle do movimento vertical
    int movimento_horizontal = 1; // Controle do movimento horizontal
    int casa_atual = 1;           // Casa atual do movimento
    
    // LOOP EXTERNO: Controla movimento vertical (cima)
    for (movimento_vertical = 1; movimento_vertical <= CASAS_BISPO; movimento_vertical++) {
        
        // LOOP INTERNO: Controla movimento horizontal (direita)
        for (movimento_horizontal = 1; movimento_horizontal <= 1; movimento_horizontal++) {
            
            // Imprime a combinação de movimentos diagonal
            printf("Casa %d: Cima, Direita\n", casa_atual);
            casa_atual++;
            
            // Uso de BREAK para sair do loop interno após 1 movimento horizontal
            break;
        }
    }
}