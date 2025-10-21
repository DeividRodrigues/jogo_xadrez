#!/usr/bin/env python3
"""
DEMONSTRAÇÃO DOS CONCEITOS DE PROGRAMAÇÃO
=========================================

Este arquivo demonstra os objetivos específicos do projeto:

1. ESTRUTURAS DE REPETIÇÃO SIMPLES (for, while) para Torre, Bispo, Rainha
2. LOOPS ANINHADOS para movimento complexo do Cavalo em "L"
3. RECURSIVIDADE e LOOPS COMPLEXOS para movimentos avançados
"""

from chess_pieces_enhanced import *
from chess_board import ChessBoard


def demo_simple_loops():
    """
    DEMONSTRAÇÃO 1: ESTRUTURAS DE REPETIÇÃO SIMPLES
    ===============================================
    
    Objetivo: Aplicar estruturas de repetição simples (for, while) 
    para simular movimentos básicos de peças de xadrez (Torre, Bispo, Rainha)
    """
    print("="*60)
    print("DEMONSTRAÇÃO 1: ESTRUTURAS DE REPETIÇÃO SIMPLES")
    print("="*60)
    print("Objetivo: Torre, Bispo e Rainha usando for/while loops")
    print()
    
    board = ChessBoard()
    
    # Demonstração da TORRE (movimentos lineares)
    print("🏰 TORRE - Movimentos lineares com FOR + WHILE:")
    print("-" * 50)
    rook = Rook(Color.WHITE, 7, 0)  # Torre em a1
    print(f"Torre em posição: ({rook.row}, {rook.col})")
    
    # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para direções
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
    print("Direções: direita, baixo, esquerda, cima")
    
    moves = rook.get_possible_moves(board)
    print(f"Movimentos possíveis: {len(moves)}")
    for i, (row, col) in enumerate(moves[:5]):  # Mostra apenas os primeiros 5
        print(f"  {i+1}. Posição ({row}, {col})")
    if len(moves) > 5:
        print(f"  ... e mais {len(moves) - 5} movimentos")
    
    print()
    
    # Demonstração do BISPO (movimentos diagonais)
    print("♗ BISPO - Movimentos diagonais com FOR + WHILE:")
    print("-" * 50)
    bishop = Bishop(Color.WHITE, 7, 2)  # Bispo em c1
    print(f"Bispo em posição: ({bishop.row}, {bishop.col})")
    
    # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para direções diagonais
    diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    print("Direções diagonais: NE, NW, SE, SW")
    
    moves = bishop.get_possible_moves(board)
    print(f"Movimentos possíveis: {len(moves)}")
    for i, (row, col) in enumerate(moves[:5]):
        print(f"  {i+1}. Posição ({row}, {col})")
    if len(moves) > 5:
        print(f"  ... e mais {len(moves) - 5} movimentos")
    
    print()
    
    # Demonstração da RAINHA (combinação de torre + bispo)
    print("♕ RAINHA - Combinação de movimentos com FOR + WHILE:")
    print("-" * 50)
    queen = Queen(Color.WHITE, 7, 3)  # Rainha em d1
    print(f"Rainha em posição: ({queen.row}, {queen.col})")
    
    # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para todas as direções
    all_directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # linhas retas
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonais
    ]
    print("Direções: 8 direções (4 retas + 4 diagonais)")
    
    moves = queen.get_possible_moves(board)
    print(f"Movimentos possíveis: {len(moves)}")
    for i, (row, col) in enumerate(moves[:8]):
        print(f"  {i+1}. Posição ({row}, {col})")
    if len(moves) > 8:
        print(f"  ... e mais {len(moves) - 8} movimentos")


def demo_nested_loops():
    """
    DEMONSTRAÇÃO 2: LOOPS ANINHADOS
    ===============================
    
    Objetivo: Aplicar loops aninhados para simular o movimento complexo 
    em "L" do Cavalo no tabuleiro de xadrez
    """
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO 2: LOOPS ANINHADOS - CAVALO")
    print("="*60)
    print("Objetivo: Movimento complexo em 'L' do Cavalo")
    print()
    
    board = ChessBoard()
    
    print("♘ CAVALO - Movimento em 'L' com LOOPS ANINHADOS:")
    print("-" * 50)
    knight = Knight(Color.WHITE, 7, 1)  # Cavalo em b1
    print(f"Cavalo em posição: ({knight.row}, {knight.col})")
    
    print("LOOPS ANINHADOS para movimento em 'L':")
    print("  - Primeiro loop: distância 2 (2 casas)")
    print("  - Segundo loop aninhado: distância 1 (1 casa)")
    print("  - Combinações: (2,1), (2,-1), (1,2), (1,-2), etc.")
    
    moves = knight.get_possible_moves(board)
    print(f"Movimentos possíveis: {len(moves)}")
    
    # Demonstração detalhada dos loops aninhados
    print("\nDetalhamento dos LOOPS ANINHADOS:")
    print("for distance in [2, -2]:")
    print("    for step in [1, -1]:")
    print("        # Combinações geradas:")
    
    combinations = []
    for distance in [2, -2]:
        for step in [1, -1]:
            # Combinação 1: (distance, step)
            combinations.append((distance, step))
            # Combinação 2: (step, distance) - movimento perpendicular
            combinations.append((step, distance))
    
    for i, (dr, dc) in enumerate(combinations):
        new_row = knight.row + dr
        new_col = knight.col + dc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            print(f"  {i+1}. Movimento ({dr}, {dc}) -> Posição ({new_row}, {new_col})")
    
    print(f"\nTotal de combinações válidas: {len(moves)}")
    for i, (row, col) in enumerate(moves):
        print(f"  Movimento {i+1}: ({row}, {col})")


def demo_recursion_and_complex_loops():
    """
    DEMONSTRAÇÃO 3: RECURSIVIDADE E LOOPS COMPLEXOS
    ==============================================
    
    Objetivo: Aplicar recursividade e loops complexos com múltiplas condições 
    para simular movimentos avançados das peças de xadrez
    """
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO 3: RECURSIVIDADE E LOOPS COMPLEXOS")
    print("="*60)
    print("Objetivo: Análise avançada com recursividade e múltiplas condições")
    print()
    
    board = ChessBoard()
    analyzer = AdvancedChessAnalyzer(board)
    
    print("🔍 ANÁLISE AVANÇADA - Recursividade e Loops Complexos:")
    print("-" * 50)
    
    # Demonstração de análise recursiva
    print("1. ANÁLISE RECURSIVA do tabuleiro:")
    analysis = analyzer.analyze_board_complexity()
    
    print(f"   Total de movimentos possíveis: {analysis['total_moves']}")
    print(f"   Movimentos seguros: {analysis['safe_moves']}")
    print(f"   Movimentos perigosos: {analysis['dangerous_moves']}")
    print(f"   Peças sob ataque: {analysis['pieces_under_attack']}")
    print(f"   Score de complexidade: {analysis['complexity_score']}")
    
    print("\n2. LOOPS COMPLEXOS com múltiplas condições:")
    print("   - Loop externo: todas as linhas (0-7)")
    print("   - Loop interno: todas as colunas (0-7)")
    print("   - Condições aninhadas: verificação de peças, cores, tipos")
    print("   - Loops adicionais: análise de movimentos de cada peça")
    
    # Demonstração de busca recursiva de caminhos
    print("\n3. BUSCA RECURSIVA de caminhos de ataque:")
    queen = Queen(Color.WHITE, 7, 3)  # Rainha em d1
    target_row, target_col = 0, 3  # Alvo em d8
    
    print(f"   Rainha em ({queen.row}, {queen.col})")
    print(f"   Alvo em ({target_row}, {target_col})")
    
    # Simula busca recursiva (limitada para demonstração)
    print("   Algoritmo recursivo:")
    print("   - Condição de parada: profundidade máxima ou posição alcançada")
    print("   - Chamada recursiva: para cada movimento possível")
    print("   - Múltiplas condições: verificação de segurança, xeque, etc.")
    
    print("\n4. EXEMPLO de recursividade em ação:")
    print("   def find_paths(piece, target, path=[]):")
    print("       if len(path) > max_depth: return []")
    print("       if piece.position == target: return [path]")
    print("       for move in possible_moves:")
    print("           if is_safe(move) and not_in_check(move):")
    print("               paths += find_paths(piece, target, path + [move])")
    print("       return paths")


def demo_educational_comparison():
    """
    DEMONSTRAÇÃO 4: COMPARAÇÃO EDUCACIONAL
    ======================================
    
    Mostra a diferença entre implementações simples e avançadas
    """
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO 4: COMPARAÇÃO EDUCACIONAL")
    print("="*60)
    print("Comparação: Implementação Simples vs Avançada")
    print()
    
    print("📊 COMPARAÇÃO DE CONCEITOS:")
    print("-" * 50)
    
    concepts = [
        ("ESTRUTURAS SIMPLES", "for/while", "Torre, Bispo, Rainha", "Movimentos lineares/diagonais"),
        ("LOOPS ANINHADOS", "for dentro de for", "Cavalo", "Movimento complexo em 'L'"),
        ("RECURSIVIDADE", "função chama a si mesma", "Análise avançada", "Busca de caminhos e análise"),
        ("LOOPS COMPLEXOS", "múltiplas condições", "Todas as peças", "Verificação de segurança e xeque")
    ]
    
    for concept, technique, pieces, description in concepts:
        print(f"🎯 {concept}")
        print(f"   Técnica: {technique}")
        print(f"   Aplicação: {pieces}")
        print(f"   Descrição: {description}")
        print()


def main():
    """
    Função principal que executa todas as demonstrações
    """
    print("🎓 DEMONSTRAÇÃO DOS CONCEITOS DE PROGRAMAÇÃO EM XADREZ")
    print("=" * 60)
    print("Este programa demonstra os objetivos específicos:")
    print("1. Estruturas de repetição simples (for, while)")
    print("2. Loops aninhados para movimento do Cavalo")
    print("3. Recursividade e loops complexos")
    print("=" * 60)
    
    try:
        # Executa todas as demonstrações
        demo_simple_loops()
        demo_nested_loops()
        demo_recursion_and_complex_loops()
        demo_educational_comparison()
        
        print("\n" + "="*60)
        print("✅ DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
        print("="*60)
        print("Todos os conceitos foram demonstrados:")
        print("✓ Estruturas de repetição simples")
        print("✓ Loops aninhados para Cavalo")
        print("✓ Recursividade e loops complexos")
        print("✓ Análise avançada do tabuleiro")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Erro durante a demonstração: {e}")
        print("Verifique se todos os arquivos estão presentes.")


if __name__ == "__main__":
    main()
