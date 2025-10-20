from abc import ABC, abstractmethod
from typing import List, Tuple
import enum


class Color(enum.Enum):
    WHITE = "white"
    BLACK = "black"


class PieceType(enum.Enum):
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"


class Piece(ABC):
    """
    Classe abstrata base para todas as peças de xadrez
    """
    
    def __init__(self, color: Color, row: int, col: int):
        self.color = color
        self.row = row
        self.col = col
        self.has_moved = False
    
    @abstractmethod
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        """
        Retorna uma lista de posições possíveis para onde a peça pode se mover
        """
        pass
    
    @abstractmethod
    def get_symbol(self) -> str:
        """
        Retorna o símbolo Unicode da peça
        """
        pass
    
    def move(self, new_row: int, new_col: int):
        """
        Move a peça para uma nova posição
        """
        self.row = new_row
        self.col = new_col
        self.has_moved = True
    
    def is_valid_position(self, row: int, col: int) -> bool:
        """
        Verifica se a posição está dentro dos limites do tabuleiro
        """
        return 0 <= row < 8 and 0 <= col < 8
    
    def is_enemy_piece(self, board, row: int, col: int) -> bool:
        """
        Verifica se há uma peça inimiga na posição especificada
        """
        piece = board.get_piece(row, col)
        return piece is not None and piece.color != self.color
    
    def is_own_piece(self, board, row: int, col: int) -> bool:
        """
        Verifica se há uma peça própria na posição especificada
        """
        piece = board.get_piece(row, col)
        return piece is not None and piece.color == self.color


class Pawn(Piece):
    """
    Classe para o peão
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        direction = -1 if self.color == Color.WHITE else 1
        
        # Movimento para frente
        new_row = self.row + direction
        if self.is_valid_position(new_row, self.col):
            if board.get_piece(new_row, self.col) is None:
                moves.append((new_row, self.col))
                
                # Movimento duplo no primeiro movimento
                if not self.has_moved:
                    new_row += direction
                    if self.is_valid_position(new_row, self.col):
                        if board.get_piece(new_row, self.col) is None:
                            moves.append((new_row, self.col))
        
        # Capturas diagonais
        for col_offset in [-1, 1]:
            new_row = self.row + direction
            new_col = self.col + col_offset
            if self.is_valid_position(new_row, new_col):
                if self.is_enemy_piece(board, new_row, new_col):
                    moves.append((new_row, new_col))
        
        return moves
    
    def get_symbol(self) -> str:
        return "♟" if self.color == Color.BLACK else "♙"


class Rook(Piece):
    """
    Classe para a torre
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
        
        for dr, dc in directions:
            row, col = self.row + dr, self.col + dc
            while self.is_valid_position(row, col):
                if board.get_piece(row, col) is None:
                    moves.append((row, col))
                elif self.is_enemy_piece(board, row, col):
                    moves.append((row, col))
                    break
                else:
                    break
                row += dr
                col += dc
        
        return moves
    
    def get_symbol(self) -> str:
        return "♜" if self.color == Color.BLACK else "♖"


class Knight(Piece):
    """
    Classe para o cavalo
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        for dr, dc in knight_moves:
            new_row, new_col = self.row + dr, self.col + dc
            if self.is_valid_position(new_row, new_col):
                if (board.get_piece(new_row, new_col) is None or 
                    self.is_enemy_piece(board, new_row, new_col)):
                    moves.append((new_row, new_col))
        
        return moves
    
    def get_symbol(self) -> str:
        return "♞" if self.color == Color.BLACK else "♘"


class Bishop(Piece):
    """
    Classe para o bispo
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # diagonais
        
        for dr, dc in directions:
            row, col = self.row + dr, self.col + dc
            while self.is_valid_position(row, col):
                if board.get_piece(row, col) is None:
                    moves.append((row, col))
                elif self.is_enemy_piece(board, row, col):
                    moves.append((row, col))
                    break
                else:
                    break
                row += dr
                col += dc
        
        return moves
    
    def get_symbol(self) -> str:
        return "♝" if self.color == Color.BLACK else "♗"


class Queen(Piece):
    """
    Classe para a rainha
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # linhas retas
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonais
        ]
        
        for dr, dc in directions:
            row, col = self.row + dr, self.col + dc
            while self.is_valid_position(row, col):
                if board.get_piece(row, col) is None:
                    moves.append((row, col))
                elif self.is_enemy_piece(board, row, col):
                    moves.append((row, col))
                    break
                else:
                    break
                row += dr
                col += dc
        
        return moves
    
    def get_symbol(self) -> str:
        return "♛" if self.color == Color.BLACK else "♕"


class King(Piece):
    """
    Classe para o rei
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # adjacentes
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonais
        ]
        
        for dr, dc in directions:
            new_row, new_col = self.row + dr, self.col + dc
            if self.is_valid_position(new_row, new_col):
                if (board.get_piece(new_row, new_col) is None or 
                    self.is_enemy_piece(board, new_row, new_col)):
                    moves.append((new_row, new_col))
        
        return moves
    
    def get_symbol(self) -> str:
        return "♚" if self.color == Color.BLACK else "♔"
