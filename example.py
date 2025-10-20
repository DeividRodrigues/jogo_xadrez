#!/usr/bin/env python3
"""
Exemplo de uso das classes do jogo de xadrez
"""

from chess_board import ChessBoard
from chess_pieces import Color


def demo_movements():
    """
    Demonstra como usar as classes para fazer movimentos
    """
    print("=== DEMO: Movimentando Peças do Xadrez ===\n")
    
    # Criar tabuleiro
    board = ChessBoard()
    
    print("Tabuleiro inicial:")
    board.display_board()
    
    print(f"\nJogador atual: {board.current_player.value}")
    
    # Mostrar movimentos possíveis das peças brancas
    print("\nMovimentos possíveis para as peças brancas:")
    moves = board.get_all_moves(Color.WHITE)
    for i, (from_row, from_col, to_row, to_col) in enumerate(moves[:10]):  # Primeiros 10
        from_pos = chr(ord('a') + from_col) + str(8 - from_row)
        to_pos = chr(ord('a') + to_col) + str(8 - to_row)
        print(f"{i+1:2d}. {from_pos}-{to_pos}")
    
    if len(moves) > 10:
        print(f"... e mais {len(moves) - 10} movimentos")
    
    # Fazer um movimento exemplo (peão e2 para e4)
    print("\n--- Fazendo movimento: e2-e4 ---")
    success = board.move_piece(6, 4, 4, 4)  # e2 (linha 6, col 4) para e4 (linha 4, col 4)
    
    if success:
        print("✅ Movimento realizado com sucesso!")
        board.display_board()
        print(f"\nPróximo jogador: {board.current_player.value}")
    else:
        print("❌ Movimento falhou!")
    
    # Tentar movimento das pretas (peão e7 para e5)
    print("\n--- Fazendo movimento das pretas: e7-e5 ---")
    success = board.move_piece(1, 4, 3, 4)  # e7 (linha 1, col 4) para e5 (linha 3, col 4)
    
    if success:
        print("✅ Movimento das pretas realizado com sucesso!")
        board.display_board()
        print(f"\nPróximo jogador: {board.current_player.value}")
    else:
        print("❌ Movimento das pretas falhou!")
    
    # Agora tentar movimento das brancas novamente (cavalo g1 para f3)
    print("\n--- Fazendo movimento das brancas: g1-f3 ---")
    success = board.move_piece(7, 6, 5, 5)  # g1 (linha 7, col 6) para f3 (linha 5, col 5)
    
    if success:
        print("✅ Movimento das brancas realizado com sucesso!")
        board.display_board()
    else:
        print("❌ Movimento das brancas falhou!")
    
    # Mostrar histórico
    print(f"\nHistórico de movimentos ({len(board.move_history)} movimentos):")
    for i, move in enumerate(board.move_history, 1):
        from_row, from_col = move['from']
        to_row, to_col = move['to']
        piece = move['piece']
        
        from_pos = chr(ord('a') + from_col) + str(8 - from_row)
        to_pos = chr(ord('a') + to_col) + str(8 - to_row)
        piece_name = type(piece).__name__
        
        print(f"{i}. {piece_name} de {piece.color.value}: {from_pos}-{to_pos}")


def demo_piece_creation():
    """
    Demonstra como criar e manipular peças individuais
    """
    print("\n=== DEMO: Criação de Peças ===\n")
    
    from chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King
    
    # Criar algumas peças
    white_pawn = Pawn(Color.WHITE, 6, 4)  # Peão branco em e2
    black_rook = Rook(Color.BLACK, 0, 0)  # Torre preta em a8
    white_knight = Knight(Color.WHITE, 7, 1)  # Cavalo branco em b1
    
    pieces = [white_pawn, black_rook, white_knight]
    
    for piece in pieces:
        print(f"{piece.get_symbol()} - {type(piece).__name__} {piece.color.value} em posição ({piece.row}, {piece.col})")


if __name__ == "__main__":
    demo_movements()
    demo_piece_creation()
    
    print("\n" + "="*50)
    print("Para jogar o jogo completo, execute: python chess_game.py")
    print("="*50)
