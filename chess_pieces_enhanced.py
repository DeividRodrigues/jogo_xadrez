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
    Demonstra conceitos de programação orientada a objetos
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
    Demonstra estruturas de repetição simples (for)
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        direction = -1 if self.color == Color.WHITE else 1
        
        # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para capturas diagonais
        for col_offset in [-1, 1]:
            new_row = self.row + direction
            new_col = self.col + col_offset
            if self.is_valid_position(new_row, new_col):
                if self.is_enemy_piece(board, new_row, new_col):
                    moves.append((new_row, new_col))
        
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
        
        return moves
    
    def get_symbol(self) -> str:
        return "♟" if self.color == Color.BLACK else "♙"


class Rook(Piece):
    """
    Classe para a torre
    Demonstra estruturas de repetição simples (for + while) para movimentos lineares
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para direções
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direita, baixo, esquerda, cima
        
        for dr, dc in directions:
            row, col = self.row + dr, self.col + dc
            # ESTRUTURA DE REPETIÇÃO SIMPLES: while loop para movimento contínuo
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
    Demonstra LOOPS ANINHADOS para movimento complexo em "L"
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        
        # LOOPS ANINHADOS para simular movimento complexo em "L"
        # Primeiro loop: variações de distância (2 casas)
        for distance in [2, -2]:
            # Segundo loop aninhado: variações de distância (1 casa)
            for step in [1, -1]:
                # Combinações: (2,1), (2,-1), (-2,1), (-2,-1)
                new_row = self.row + distance
                new_col = self.col + step
                
                if self.is_valid_position(new_row, new_col):
                    if (board.get_piece(new_row, new_col) is None or 
                        self.is_enemy_piece(board, new_row, new_col)):
                        moves.append((new_row, new_col))
                
                # Combinações: (1,2), (1,-2), (-1,2), (-1,-2)
                new_row = self.row + step
                new_col = self.col + distance
                
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
    Demonstra estruturas de repetição simples (for + while) para movimentos diagonais
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para direções diagonais
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # diagonais
        
        for dr, dc in directions:
            row, col = self.row + dr, self.col + dc
            # ESTRUTURA DE REPETIÇÃO SIMPLES: while loop para movimento contínuo
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
    Demonstra estruturas de repetição simples (for + while) combinando torre e bispo
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para todas as direções
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # linhas retas (como torre)
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonais (como bispo)
        ]
        
        for dr, dc in directions:
            row, col = self.row + dr, self.col + dc
            # ESTRUTURA DE REPETIÇÃO SIMPLES: while loop para movimento contínuo
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
    Demonstra estruturas de repetição simples (for) para movimento limitado
    """
    
    def get_possible_moves(self, board) -> List[Tuple[int, int]]:
        moves = []
        # ESTRUTURA DE REPETIÇÃO SIMPLES: for loop para direções adjacentes
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


class AdvancedChessAnalyzer:
    """
    Classe que demonstra RECURSIVIDADE e LOOPS COMPLEXOS para análise avançada
    """
    
    def __init__(self, board):
        self.board = board
        self.visited_positions = set()
        self.analysis_depth = 0
        self.max_depth = 3
    
    def find_all_attack_paths(self, piece, target_row: int, target_col: int, 
                              current_path: List[Tuple[int, int]] = None) -> List[List[Tuple[int, int]]]:
        """
        RECURSIVIDADE: Encontra todos os caminhos de ataque possíveis
        Demonstra recursividade com múltiplas condições
        """
        if current_path is None:
            current_path = []
        
        # Condição de parada da recursão
        if len(current_path) > self.max_depth:
            return []
        
        if piece.row == target_row and piece.col == target_col:
            return [current_path.copy()]
        
        paths = []
        possible_moves = piece.get_possible_moves(self.board)
        
        # LOOP COMPLEXO com múltiplas condições
        for move_row, move_col in possible_moves:
            # Múltiplas condições para evitar loops infinitos
            if (move_row, move_col) not in self.visited_positions:
                if self.is_safe_move(piece, move_row, move_col):
                    if not self.would_put_king_in_check(piece, move_row, move_col):
                        
                        # Chamada recursiva
                        self.visited_positions.add((move_row, move_col))
                        current_path.append((move_row, move_col))
                        
                        # Simula o movimento para análise recursiva
                        original_row, original_col = piece.row, piece.col
                        piece.row, piece.col = move_row, move_col
                        
                        sub_paths = self.find_all_attack_paths(piece, target_row, target_col, current_path)
                        paths.extend(sub_paths)
                        
                        # Restaura a posição original
                        piece.row, piece.col = original_row, original_col
                        current_path.pop()
                        self.visited_positions.remove((move_row, move_col))
        
        return paths
    
    def is_safe_move(self, piece, row: int, col: int) -> bool:
        """
        Verifica se um movimento é seguro
        Demonstra loops complexos com múltiplas condições
        """
        # LOOP COMPLEXO: verifica todas as peças inimigas
        for enemy_row in range(8):
            for enemy_col in range(8):
                enemy_piece = self.board.get_piece(enemy_row, enemy_col)
                
                # Múltiplas condições aninhadas
                if (enemy_piece is not None and 
                    enemy_piece.color != piece.color and
                    not isinstance(enemy_piece, King)):
                    
                    enemy_moves = enemy_piece.get_possible_moves(self.board)
                    
                    # LOOP ANINHADO: verifica se a posição seria atacada
                    for enemy_move_row, enemy_move_col in enemy_moves:
                        if enemy_move_row == row and enemy_move_col == col:
                            return False
        
        return True
    
    def would_put_king_in_check(self, piece, row: int, col: int) -> bool:
        """
        Verifica se um movimento colocaria o rei em xeque
        Demonstra recursividade e loops complexos
        """
        # Simula o movimento temporariamente
        original_row, original_col = piece.row, piece.col
        original_piece_at_destination = self.board.get_piece(row, col)
        
        # Faz o movimento temporário
        piece.row, piece.col = row, col
        self.board.board[original_row][original_col] = None
        self.board.board[row][col] = piece
        
        # Encontra o rei do jogador
        king_found = False
        king_row, king_col = -1, -1
        
        # LOOP COMPLEXO: procura o rei
        for search_row in range(8):
            for search_col in range(8):
                king_piece = self.board.get_piece(search_row, search_col)
                if (king_piece is not None and 
                    isinstance(king_piece, King) and 
                    king_piece.color == piece.color):
                    king_row, king_col = search_row, search_col
                    king_found = True
                    break
            if king_found:
                break
        
        # Verifica se o rei estaria em xeque
        in_check = False
        if king_found:
            # LOOP COMPLEXO: verifica todas as peças inimigas
            for enemy_row in range(8):
                for enemy_col in range(8):
                    enemy_piece = self.board.get_piece(enemy_row, enemy_col)
                    if (enemy_piece is not None and 
                        enemy_piece.color != piece.color):
                        enemy_moves = enemy_piece.get_possible_moves(self.board)
                        for enemy_move_row, enemy_move_col in enemy_moves:
                            if enemy_move_row == king_row and enemy_move_col == king_col:
                                in_check = True
                                break
                    if in_check:
                        break
        
        # Restaura o estado original
        piece.row, piece.col = original_row, original_col
        self.board.board[original_row][original_col] = piece
        self.board.board[row][col] = original_piece_at_destination
        
        return in_check
    
    def analyze_board_complexity(self) -> dict:
        """
        RECURSIVIDADE e LOOPS COMPLEXOS: Análise completa do tabuleiro
        """
        analysis = {
            'total_moves': 0,
            'safe_moves': 0,
            'dangerous_moves': 0,
            'pieces_under_attack': 0,
            'complexity_score': 0
        }
        
        # LOOP COMPLEXO: analisa todas as peças
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece(row, col)
                if piece is not None:
                    moves = piece.get_possible_moves(self.board)
                    analysis['total_moves'] += len(moves)
                    
                    # LOOP ANINHADO: analisa cada movimento
                    for move_row, move_col in moves:
                        if self.is_safe_move(piece, move_row, move_col):
                            analysis['safe_moves'] += 1
                        else:
                            analysis['dangerous_moves'] += 1
                    
                    # Verifica se a peça está sob ataque
                    if self.is_piece_under_attack(piece):
                        analysis['pieces_under_attack'] += 1
        
        # Calcula score de complexidade usando recursividade
        analysis['complexity_score'] = self._calculate_complexity_score(analysis)
        
        return analysis
    
    def _calculate_complexity_score(self, analysis: dict, depth: int = 0) -> int:
        """
        RECURSIVIDADE: Calcula score de complexidade recursivamente
        """
        if depth > 5:  # Condição de parada
            return 0
        
        base_score = (analysis['total_moves'] * 2 + 
                     analysis['dangerous_moves'] * 3 + 
                     analysis['pieces_under_attack'] * 5)
        
        # Chamada recursiva com profundidade
        if depth < 3:
            recursive_score = self._calculate_complexity_score(analysis, depth + 1)
            return base_score + recursive_score // 2
        
        return base_score
    
    def is_piece_under_attack(self, piece) -> bool:
        """
        Verifica se uma peça está sob ataque
        Demonstra loops complexos com múltiplas condições
        """
        # LOOP COMPLEXO: verifica todas as peças inimigas
        for enemy_row in range(8):
            for enemy_col in range(8):
                enemy_piece = self.board.get_piece(enemy_row, enemy_col)
                
                # Múltiplas condições aninhadas
                if (enemy_piece is not None and 
                    enemy_piece.color != piece.color):
                    
                    enemy_moves = enemy_piece.get_possible_moves(self.board)
                    
                    # LOOP ANINHADO: verifica se pode atacar a peça
                    for enemy_move_row, enemy_move_col in enemy_moves:
                        if enemy_move_row == piece.row and enemy_move_col == piece.col:
                            return True
        
        return False
