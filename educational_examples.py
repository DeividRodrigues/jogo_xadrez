#!/usr/bin/env python3
"""
EXEMPLOS EDUCACIONAIS - CONCEITOS DE PROGRAMAÇÃO
===============================================

Este arquivo contém exemplos práticos e educacionais que demonstram
claramente os conceitos solicitados nos objetivos do projeto.
"""

def exemplo_1_estruturas_simples():
    """
    EXEMPLO 1: ESTRUTURAS DE REPETIÇÃO SIMPLES
    ==========================================
    
    Demonstra for e while loops para Torre, Bispo e Rainha
    """
    print("📚 EXEMPLO 1: ESTRUTURAS DE REPETIÇÃO SIMPLES")
    print("=" * 50)
    
    # EXEMPLO A: FOR LOOP para Torre (movimentos lineares)
    print("🏰 TORRE - FOR LOOP para direções:")
    print("directions = [(0,1), (1,0), (0,-1), (-1,0)]")
    print("for dr, dc in directions:")
    print("    # Move na direção até encontrar obstáculo")
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i, (dr, dc) in enumerate(directions):
        direction_names = ["direita", "baixo", "esquerda", "cima"]
        print(f"  {i+1}. Direção {direction_names[i]}: ({dr}, {dc})")
    
    print()
    
    # EXEMPLO B: WHILE LOOP para movimento contínuo
    print("♗ BISPO - WHILE LOOP para movimento contínuo:")
    print("while is_valid_position(row, col):")
    print("    if board.get_piece(row, col) is None:")
    print("        moves.append((row, col))")
    print("    else:")
    print("        break")
    print("    row += dr")
    print("    col += dc")
    
    # Simulação de movimento diagonal
    print("\nSimulação de movimento diagonal:")
    row, col = 3, 3  # Posição inicial
    dr, dc = 1, 1    # Direção diagonal (sudeste)
    moves = []
    
    print(f"Posição inicial: ({row}, {col})")
    print(f"Direção: ({dr}, {dc})")
    
    step = 0
    while step < 4:  # Simula movimento até encontrar obstáculo
        row += dr
        col += dc
        step += 1
        print(f"  Passo {step}: posição ({row}, {col})")
        if step >= 3:  # Simula obstáculo
            print("  → Encontrou obstáculo, para aqui")
            break
    
    print()


def exemplo_2_loops_aninhados():
    """
    EXEMPLO 2: LOOPS ANINHADOS
    =========================
    
    Demonstra loops aninhados para movimento complexo do Cavalo
    """
    print("📚 EXEMPLO 2: LOOPS ANINHADOS - CAVALO")
    print("=" * 50)
    
    print("♘ CAVALO - LOOPS ANINHADOS para movimento em 'L':")
    print()
    
    # ESTRUTURA DOS LOOPS ANINHADOS
    print("ESTRUTURA DOS LOOPS ANINHADOS:")
    print("for distance in [2, -2]:")
    print("    for step in [1, -1]:")
    print("        # Combinações geradas:")
    print("        # (distance, step) e (step, distance)")
    print()
    
    print("DEMONSTRAÇÃO PRÁTICA:")
    print("-" * 30)
    
    # Primeiro loop: distâncias principais
    for distance in [2, -2]:
        print(f"🔹 Loop externo: distance = {distance}")
        
        # Segundo loop aninhado: passos
        for step in [1, -1]:
            print(f"  🔸 Loop interno: step = {step}")
            
            # Combinação 1: (distance, step)
            combo1 = (distance, step)
            print(f"    → Combinação 1: {combo1}")
            
            # Combinação 2: (step, distance) - perpendicular
            combo2 = (step, distance)
            print(f"    → Combinação 2: {combo2}")
            
            print(f"    → Total: 2 movimentos em 'L'")
        print()
    
    print("RESULTADO: 8 movimentos possíveis em 'L'")
    print("(2 distâncias × 2 passos × 2 orientações = 8)")


def exemplo_3_recursividade():
    """
    EXEMPLO 3: RECURSIVIDADE
    =========================
    
    Demonstra recursividade para análise avançada
    """
    print("📚 EXEMPLO 3: RECURSIVIDADE")
    print("=" * 50)
    
    print("🔍 RECURSIVIDADE - Análise de caminhos:")
    print()
    
    # Exemplo de função recursiva
    def contar_movimentos_recursivo(profundidade, max_profundidade):
        """
        Função recursiva que demonstra o conceito
        """
        print(f"  📍 Profundidade {profundidade}")
        
        # Condição de parada
        if profundidade >= max_profundidade:
            print(f"  🛑 Parada: profundidade máxima ({max_profundidade}) atingida")
            return 1
        
        # Chamada recursiva
        print(f"  🔄 Chamada recursiva para profundidade {profundidade + 1}")
        resultado = contar_movimentos_recursivo(profundidade + 1, max_profundidade)
        
        print(f"  📊 Retornando: {resultado} movimentos")
        return resultado + 1
    
    print("EXEMPLO DE RECURSIVIDADE:")
    print("-" * 30)
    print("def analisar_movimentos(profundidade):")
    print("    if profundidade >= max_profundidade:")
    print("        return 1")
    print("    return analisar_movimentos(profundidade + 1) + 1")
    print()
    
    print("EXECUÇÃO:")
    resultado = contar_movimentos_recursivo(0, 3)
    print(f"\nRESULTADO FINAL: {resultado} movimentos analisados")
    
    print()
    print("CARACTERÍSTICAS DA RECURSIVIDADE:")
    print("✓ Função chama a si mesma")
    print("✓ Condição de parada definida")
    print("✓ Cada chamada tem parâmetros diferentes")
    print("✓ Resultado é construído de volta")


def exemplo_4_loops_complexos():
    """
    EXEMPLO 4: LOOPS COMPLEXOS COM MÚLTIPLAS CONDIÇÕES
    ==================================================
    
    Demonstra loops complexos para análise avançada
    """
    print("📚 EXEMPLO 4: LOOPS COMPLEXOS")
    print("=" * 50)
    
    print("🔍 LOOPS COMPLEXOS - Análise de segurança:")
    print()
    
    # Simulação de tabuleiro 3x3 para demonstração
    tabuleiro = [
        ['T', 'C', 'B'],
        ['P', 'R', 'P'],
        ['B', 'C', 'T']
    ]
    
    print("TABULEIRO SIMULADO (3x3):")
    for i, linha in enumerate(tabuleiro):
        print(f"  Linha {i}: {linha}")
    print()
    
    print("LOOP COMPLEXO - Verificação de segurança:")
    print("-" * 40)
    
    pecas_sob_ataque = 0
    total_verificacoes = 0
    
    # LOOP EXTERNO: todas as linhas
    for linha in range(3):
        print(f"🔹 Linha {linha}:")
        
        # LOOP INTERNO: todas as colunas
        for coluna in range(3):
            peca = tabuleiro[linha][coluna]
            print(f"  🔸 Coluna {coluna}: peça '{peca}'")
            
            # MÚLTIPLAS CONDIÇÕES ANINHADAS
            if peca != '.':
                print(f"    → Peça encontrada: {peca}")
                
                # LOOP ADICIONAL: verifica ataques
                ataques = 0
                for linha_ataque in range(3):
                    for coluna_ataque in range(3):
                        peca_ataque = tabuleiro[linha_ataque][coluna_ataque]
                        
                        # MÚLTIPLAS CONDIÇÕES
                        if (peca_ataque != '.' and 
                            peca_ataque != peca and
                            (linha_ataque != linha or coluna_ataque != coluna)):
                            
                            ataques += 1
                            print(f"      ⚔️  Ataque de {peca_ataque} em ({linha_ataque},{coluna_ataque})")
                
                if ataques > 0:
                    pecas_sob_ataque += 1
                    print(f"    ⚠️  Peça {peca} está sob {ataques} ataque(s)")
                else:
                    print(f"    ✅ Peça {peca} está segura")
            
            total_verificacoes += 1
    
    print(f"\nRESULTADO DA ANÁLISE:")
    print(f"  Total de verificações: {total_verificacoes}")
    print(f"  Peças sob ataque: {pecas_sob_ataque}")
    print(f"  Peças seguras: {total_verificacoes - pecas_sob_ataque}")


def exemplo_5_comparacao_conceitos():
    """
    EXEMPLO 5: COMPARAÇÃO DOS CONCEITOS
    ====================================
    
    Compara e resume todos os conceitos demonstrados
    """
    print("📚 EXEMPLO 5: COMPARAÇÃO DOS CONCEITOS")
    print("=" * 50)
    
    conceitos = [
        {
            "nome": "ESTRUTURAS SIMPLES",
            "tecnica": "for/while",
            "aplicacao": "Torre, Bispo, Rainha",
            "complexidade": "Baixa",
            "exemplo": "for direction in directions:"
        },
        {
            "nome": "LOOPS ANINHADOS", 
            "tecnica": "for dentro de for",
            "aplicacao": "Cavalo",
            "complexidade": "Média",
            "exemplo": "for i in range(n): for j in range(m):"
        },
        {
            "nome": "RECURSIVIDADE",
            "tecnica": "função chama a si mesma",
            "aplicacao": "Análise de caminhos",
            "complexidade": "Alta",
            "exemplo": "def func(n): return func(n-1)"
        },
        {
            "nome": "LOOPS COMPLEXOS",
            "tecnica": "múltiplas condições",
            "aplicacao": "Análise de segurança",
            "complexidade": "Muito Alta",
            "exemplo": "for i in range(n): if cond1: for j in range(m): if cond2:"
        }
    ]
    
    print("COMPARAÇÃO DOS CONCEITOS:")
    print("-" * 50)
    
    for i, conceito in enumerate(conceitos, 1):
        print(f"{i}. {conceito['nome']}")
        print(f"   Técnica: {conceito['tecnica']}")
        print(f"   Aplicação: {conceito['aplicacao']}")
        print(f"   Complexidade: {conceito['complexidade']}")
        print(f"   Exemplo: {conceito['exemplo']}")
        print()
    
    print("RESUMO EDUCACIONAL:")
    print("-" * 30)
    print("✓ Estruturas simples: base para movimentos básicos")
    print("✓ Loops aninhados: essenciais para movimentos complexos")
    print("✓ Recursividade: poderosa para análise profunda")
    print("✓ Loops complexos: necessários para validações avançadas")
    print()
    print("🎯 OBJETIVOS ATINGIDOS:")
    print("✓ Torre, Bispo, Rainha: estruturas simples")
    print("✓ Cavalo: loops aninhados")
    print("✓ Análise avançada: recursividade + loops complexos")


def main():
    """
    Função principal que executa todos os exemplos educacionais
    """
    print("🎓 EXEMPLOS EDUCACIONAIS - CONCEITOS DE PROGRAMAÇÃO")
    print("=" * 60)
    print("Demonstração prática dos objetivos do projeto")
    print("=" * 60)
    
    try:
        exemplo_1_estruturas_simples()
        print("\n" + "="*60)
        
        exemplo_2_loops_aninhados()
        print("\n" + "="*60)
        
        exemplo_3_recursividade()
        print("\n" + "="*60)
        
        exemplo_4_loops_complexos()
        print("\n" + "="*60)
        
        exemplo_5_comparacao_conceitos()
        
        print("\n" + "="*60)
        print("✅ TODOS OS EXEMPLOS EXECUTADOS COM SUCESSO!")
        print("="*60)
        print("Conceitos demonstrados:")
        print("✓ Estruturas de repetição simples")
        print("✓ Loops aninhados para Cavalo")
        print("✓ Recursividade para análise")
        print("✓ Loops complexos para validações")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Erro durante execução: {e}")


if __name__ == "__main__":
    main()
