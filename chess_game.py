#!/usr/bin/env python3
"""
Jogo de Xadrez - Interface de Linha de Comando
"""

import sys
import re
from typing import Tuple, Optional
from chess_board import ChessBoard
from chess_pieces import Color, Piece


class ChessGame:
    """
    Classe principal que gerencia o jogo de xadrez
    """
    
    def __init__(self):
        self.board = ChessBoard()
        self.running = True
    
    def parse_move(self, move_input: str) -> Optional[Tuple[int, int, int, int]]:
        """
        Converte notação de xadrez (ex: 'e2-e4') para coordenadas do tabuleiro
        Formato: (from_row, from_col, to_row, to_col)
        """
        # Remove espaços em branco
        move_input = move_input.strip()
        
        # Padrões aceitos:
        # e2-e4, e2 e4, e2e4
        patterns = [
            r'^([a-h])([1-8])[-\s]*([a-h])([1-8])$',
            r'^([a-h])([1-8])([a-h])([1-8])$'
        ]
        
        for pattern in patterns:
            match = re.match(pattern, move_input.lower())
            if match:
                groups = match.groups()
                if len(groups) == 4:
                    from_col = ord(groups[0]) - ord('a')
                    from_row = 8 - int(groups[1])
                    to_col = ord(groups[2]) - ord('a')
                    to_row = 8 - int(groups[3])
                    
                    # Valida se as coordenadas estão dentro dos limites
                    if all(0 <= coord < 8 for coord in [from_row, from_col, to_row, to_col]):
                        return (from_row, from_col, to_row, to_col)
        
        return None
    
    def get_piece_notation(self, row: int, col: int) -> str:
        """
        Converte coordenadas do tabuleiro para notação de xadrez
        """
        piece = self.board.get_piece(row, col)
        if piece is None:
            return "   "
        
        col_letter = chr(ord('a') + col)
        row_number = 8 - row
        
        piece_symbols = {
            'pawn': 'P' if piece.color == Color.WHITE else 'p',
            'rook': 'R' if piece.color == Color.WHITE else 'r',
            'knight': 'N' if piece.color == Color.WHITE else 'n',
            'bishop': 'B' if piece.color == Color.WHITE else 'b',
            'queen': 'Q' if piece.color == Color.WHITE else 'q',
            'king': 'K' if piece.color == Color.WHITE else 'k'
        }
        
        piece_type = type(piece).__name__.lower().replace(' ', '')
        symbol = piece_symbols.get(piece_type, '?')
        return f"{symbol}{col_letter}{row_number}"
    
    def show_help(self):
        """
        Exibe as instruções do jogo
        """
        print("\n" + "="*50)
        print("           INSTRUÇÕES DO JOGO DE XADREZ")
        print("="*50)
        print("\nComo jogar:")
        print("• Digite movimentos no formato: origem-destino")
        print("• Exemplo: e2-e4 (move peão de e2 para e4)")
        print("• Use coordenadas de xadrez: a-h (colunas), 1-8 (linhas)")
        print("\nComandos especiais:")
        print("• 'help' ou 'h' - Exibe esta ajuda")
        print("• 'quit' ou 'q' - Sai do jogo")
        print("• 'reset' ou 'r' - Reinicia o jogo")
        print("• 'history' - Mostra histórico de movimentos")
        print("• 'moves' - Mostra movimentos possíveis")
        print("\nPeças:")
        print("Brancas: ♔♕♖♗♘♙  |  Pretas: ♚♛♜♝♞♟")
        print("="*50)
    
    def show_move_history(self):
        """
        Exibe o histórico de movimentos
        """
        if not self.board.move_history:
            print("\nNenhum movimento realizado ainda.")
            return
        
        print(f"\nHistórico de movimentos ({len(self.board.move_history)} movimentos):")
        print("-" * 40)
        
        for i, move in enumerate(self.board.move_history, 1):
            from_row, from_col = move['from']
            to_row, to_col = move['to']
            piece = move['piece']
            captured = move['captured']
            
            from_pos = chr(ord('a') + from_col) + str(8 - from_row)
            to_pos = chr(ord('a') + to_col) + str(8 - to_row)
            
            move_str = f"{i:2d}. {from_pos}-{to_pos}"
            if captured:
                move_str += f" (captura {captured.get_symbol()})"
            
            player = "Brancas" if piece.color == Color.WHITE else "Pretas"
            print(f"{move_str} ({player})")
    
    def show_possible_moves(self):
        """
        Exibe os movimentos possíveis para o jogador atual
        """
        moves = self.board.get_all_moves(self.board.current_player)
        
        if not moves:
            print(f"\nNenhum movimento disponível para {self.board.current_player.value}!")
            return
        
        print(f"\nMovimentos possíveis para {self.board.current_player.value}:")
        print("-" * 40)
        
        for i, (from_row, from_col, to_row, to_col) in enumerate(moves, 1):
            from_pos = chr(ord('a') + from_col) + str(8 - from_row)
            to_pos = chr(ord('a') + to_col) + str(8 - to_row)
            
            piece = self.board.get_piece(from_row, from_col)
            piece_name = type(piece).__name__.lower()
            
            move_str = f"{i:2d}. {piece_name}: {from_pos}-{to_pos}"
            print(move_str)
            
            if i % 10 == 0 and i < len(moves):
                input("Pressione Enter para continuar...")
    
    def run(self):
        """
        Loop principal do jogo
        """
        print("\n" + "="*50)
        print("         🏁 BEM-VINDO AO JOGO DE XADREZ! 🏁")
        print("="*50)
        
        self.show_help()
        
        while self.running and not self.board.game_over:
            try:
                print(f"\n{'-'*20} Tabuleiro {'-'*20}")
                self.board.display_board()
                
                current_player_name = "Brancas" if self.board.current_player == Color.WHITE else "Pretas"
                print(f"\nVez das {current_player_name}")
                
                move_input = input("\nDigite seu movimento (ou 'help' para ajuda): ").strip()
                
                if not move_input:
                    continue
                
                # Comandos especiais
                if move_input.lower() in ['quit', 'q', 'sair']:
                    print("\nObrigado por jogar! 🎮")
                    self.running = False
                    break
                
                elif move_input.lower() in ['help', 'h', 'ajuda']:
                    self.show_help()
                    continue
                
                elif move_input.lower() in ['reset', 'r', 'reiniciar']:
                    self.board.reset_board()
                    print("\n🔄 Jogo reiniciado!")
                    continue
                
                elif move_input.lower() in ['history', 'histórico']:
                    self.show_move_history()
                    continue
                
                elif move_input.lower() in ['moves', 'movimentos']:
                    self.show_possible_moves()
                    continue
                
                # Tentar fazer o movimento
                parsed_move = self.parse_move(move_input)
                
                if parsed_move is None:
                    print("\n❌ Movimento inválido! Use o formato: e2-e4")
                    print("   Digite 'help' para ver as instruções.")
                    continue
                
                from_row, from_col, to_row, to_col = parsed_move
                
                # Verificar se há uma peça na posição de origem
                piece = self.board.get_piece(from_row, from_col)
                if piece is None:
                    print(f"\n❌ Não há peça na posição {chr(ord('a') + from_col)}{8 - from_row}")
                    continue
                
                # Verificar se a peça pertence ao jogador atual
                if piece.color != self.board.current_player:
                    print(f"\n❌ Essa peça não pertence a você!")
                    continue
                
                # Tentar fazer o movimento
                if self.board.move_piece(from_row, from_col, to_row, to_col):
                    from_pos = chr(ord('a') + from_col) + str(8 - from_row)
                    to_pos = chr(ord('a') + to_col) + str(8 - to_row)
                    print(f"\n✅ Movimento realizado: {from_pos}-{to_pos}")
                    
                    # Verificar se o jogo terminou
                    if self.board.game_over:
                        print(f"\n🏆 GAME OVER! {self.board.winner.value} venceu!")
                        break
                    
                else:
                    print("\n❌ Movimento inválido! Verifique se:")
                    print("   - A peça pode se mover para essa posição")
                    print("   - Não está capturando sua própria peça")
                    print("   - O caminho não está bloqueado")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrompido pelo usuário. Obrigado por jogar!")
                break
            
            except Exception as e:
                print(f"\n❌ Erro inesperado: {e}")
                continue
        
        if self.board.game_over and self.running:
            print("\n🎉 Partida finalizada!")
            self.show_move_history()


def main():
    """
    Função principal
    """
    try:
        game = ChessGame()
        game.run()
    except Exception as e:
        print(f"Erro fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
