/*
 * DESAFIO: Movimentando as Peças do Xadrez
 * ========================================
 * 
 * Este programa simula o movimento de três peças de xadrez:
 * - Torre: Move-se em linha reta (horizontal/vertical)
 * - Bispo: Move-se na diagonal
 * - Rainha: Move-se em todas as direções
 * 
 * Cada peça utiliza uma estrutura de repetição diferente:
 * - Torre: FOR loop
 * - Bispo: WHILE loop  
 * - Rainha: DO-WHILE loop
 * 
 * Autor: Deivid Rodrigues
 * Data: 2025
 */

#include <stdio.h>
#include <stdlib.h>

int main() {
    // Declaração de variáveis
    int i;                    // Contador para loops
    int casas_torre = 5;      // Número de casas para Torre (direita)
    int casas_bispo = 5;      // Número de casas para Bispo (diagonal)
    int casas_rainha = 8;     // Número de casas para Rainha (esquerda)
    int contador_bispo = 0;   // Contador para movimento do Bispo
    int contador_rainha = 0;  // Contador para movimento da Rainha
    
    printf("========================================\n");
    printf("    SIMULACAO DE MOVIMENTOS DE XADREZ   \n");
    printf("========================================\n\n");
    
    /*
     * TORRE - Movimento em linha reta para a direita
     * Utiliza estrutura FOR para simular movimento horizontal
     */
    printf("PEÇA: TORRE\n");
    printf("Movimento: %d casas para a DIREITA\n", casas_torre);
    printf("Estrutura de repetição: FOR\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    
    // FOR LOOP: Torre move-se para a direita
    for (i = 1; i <= casas_torre; i++) {
        printf("Casa %d: Direita\n", i);
    }
    
    printf("\n");
    
    /*
     * BISPO - Movimento na diagonal (cima e direita)
     * Utiliza estrutura WHILE para simular movimento diagonal
     */
    printf("PEÇA: BISPO\n");
    printf("Movimento: %d casas na DIAGONAL (cima e direita)\n", casas_bispo);
    printf("Estrutura de repetição: WHILE\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    
    // WHILE LOOP: Bispo move-se na diagonal
    contador_bispo = 1;
    while (contador_bispo <= casas_bispo) {
        printf("Casa %d: Cima, Direita\n", contador_bispo);
        contador_bispo++;
    }
    
    printf("\n");
    
    /*
     * RAINHA - Movimento para a esquerda
     * Utiliza estrutura DO-WHILE para simular movimento horizontal
     */
    printf("PEÇA: RAINHA\n");
    printf("Movimento: %d casas para a ESQUERDA\n", casas_rainha);
    printf("Estrutura de repetição: DO-WHILE\n");
    printf("Direção do movimento:\n");
    printf("------------------------\n");
    
    // DO-WHILE LOOP: Rainha move-se para a esquerda
    contador_rainha = 1;
    do {
        printf("Casa %d: Esquerda\n", contador_rainha);
        contador_rainha++;
    } while (contador_rainha <= casas_rainha);
    
    printf("\n");
    
    /*
     * RESUMO DOS MOVIMENTOS
     */
    printf("========================================\n");
    printf("           RESUMO DOS MOVIMENTOS       \n");
    printf("========================================\n");
    printf("Torre:   %d casas para a DIREITA (FOR)\n", casas_torre);
    printf("Bispo:   %d casas na DIAGONAL (WHILE)\n", casas_bispo);
    printf("Rainha:  %d casas para a ESQUERDA (DO-WHILE)\n", casas_rainha);
    printf("========================================\n");
    
    printf("\nSimulacao concluida com sucesso!\n");
    printf("Todas as pecas executaram seus movimentos.\n");
    
    return 0;
}
