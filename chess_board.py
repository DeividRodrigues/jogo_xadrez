from typing import Optional, List, Tuple
from chess_pieces import (
    Piece, Pawn, Rook, Knight, Bishop, Queen, King, 
    Color, PieceType
)


class ChessBoard:
    """
    Classe que representa o tabuleiro de xadrez
    """
    
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_player = Color.WHITE
        self.game_over = False
        self.winner = None
        self.move_history = []
        self._initialize_pieces()
    
    def _initialize_pieces(self):
        """
        Inicializa o tabuleiro com as peças nas posições iniciais
        """
        # Peças pretas (linha 0 e 1)
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        
        for col in range(8):
            # Torres, Cavalos, Bispos e Rainha/Rei
            self.board[0][col] = piece_order[col](Color.BLACK, 0, col)
            # Peões
            self.board[1][col] = Pawn(Color.BLACK, 1, col)
        
        # Peças brancas (linha 6 e 7)
        for col in range(8):
            # Peões
            self.board[6][col] = Pawn(Color.WHITE, 6, col)
            # Torres, Cavalos, Bispos e Rainha/Rei
            self.board[7][col] = piece_order[col](Color.WHITE, 7, col)
    
    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        """
        Retorna a peça na posição especificada ou None se não houver peça
        """
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def move_piece(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
        """
        Move uma peça de uma posição para outra
        Retorna True se o movimento for válido, False caso contrário
        """
        piece = self.get_piece(from_row, from_col)
        
        if piece is None:
            return False
        
        # Verifica se é a vez do jogador correto
        if piece.color != self.current_player:
            return False
        
        # Verifica se o movimento é válido
        if not self.is_valid_move(piece, to_row, to_col):
            return False
        
        # Captura a peça se houver uma na posição de destino
        captured_piece = self.get_piece(to_row, to_col)
        
        # Faz o movimento
        self.board[from_row][from_col] = None
        self.board[to_row][to_col] = piece
        piece.move(to_row, to_col)
        
        # Registra o movimento no histórico
        move_info = {
            'from': (from_row, from_col),
            'to': (to_row, to_col),
            'piece': piece,
            'captured': captured_piece
        }
        self.move_history.append(move_info)
        
        # Verifica se o jogo terminou
        if self.is_checkmate():
            self.game_over = True
            self.winner = self.current_player
        
        # Alterna o jogador
        self.current_player = Color.BLACK if self.current_player == Color.WHITE else Color.WHITE
        
        return True
    
    def is_valid_move(self, piece: Piece, to_row: int, to_col: int) -> bool:
        """
        Verifica se um movimento é válido
        """
        # Verifica se a posição está dentro dos limites
        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            return False
        
        # Verifica se não está tentando capturar sua própria peça
        target_piece = self.get_piece(to_row, to_col)
        if target_piece is not None and target_piece.color == piece.color:
            return False
        
        # Verifica se o movimento está na lista de movimentos possíveis da peça
        possible_moves = piece.get_possible_moves(self)
        return (to_row, to_col) in possible_moves
    
    def is_checkmate(self) -> bool:
        """
        Verifica se o jogador atual está em xeque-mate
        (Implementação simplificada - verifica apenas se o rei foi capturado)
        """
        # Procura pelo rei do jogador atual
        king_found = False
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None and isinstance(piece, King) and piece.color == self.current_player:
                    king_found = True
                    break
            if king_found:
                break
        
        return not king_found
    
    def get_all_moves(self, color: Color) -> List[Tuple[int, int, int, int]]:
        """
        Retorna todos os movimentos possíveis para um jogador
        Formato: (from_row, from_col, to_row, to_col)
        """
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None and piece.color == color:
                    possible_moves = piece.get_possible_moves(self)
                    for to_row, to_col in possible_moves:
                        if self.is_valid_move(piece, to_row, to_col):
                            moves.append((row, col, to_row, to_col))
        return moves
    
    def display_board(self):
        """
        Exibe o tabuleiro no console
        """
        print("  " + " ".join([chr(ord('a') + i) for i in range(8)]))
        for row in range(8):
            print(f"{8 - row} ", end="")
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    # Alterna entre caracteres para criar padrão do tabuleiro
                    symbol = "▓" if (row + col) % 2 == 0 else "░"
                    print(symbol + " ", end="")
                else:
                    print(piece.get_symbol() + " ", end="")
            print(f" {8 - row}")
        print("  " + " ".join([chr(ord('a') + i) for i in range(8)]))
    
    def get_board_state(self) -> str:
        """
        Retorna uma representação string do estado atual do tabuleiro
        """
        state = ""
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    state += "."
                else:
                    symbol = piece.get_symbol()
                    state += symbol
            state += "\n"
        return state
    
    def reset_board(self):
        """
        Reinicia o tabuleiro para a posição inicial
        """
        self.__init__()
