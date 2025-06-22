# Tic Tac Toe Game Logic - Enhanced Version

def check_winner(board, player):
    """
    Verifica si un jugador ha ganado
    Retorna True si el jugador tiene tres en línea
    """
    # Verificar filas
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Verificar columnas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Verificar diagonal principal (arriba-izquierda a abajo-derecha)
    if all(board[i][i] == player for i in range(3)):
        return True
    
    # Verificar diagonal secundaria (arriba-derecha a abajo-izquierda)
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    """
    Verifica si el juego terminó en empate
    Retorna True si todas las casillas están llenas y no hay ganador
    """
    return all(cell != "" for row in board for cell in row)

def get_winning_line(board, player):
    """
    Retorna las coordenadas de la línea ganadora
    Útil para resaltar la línea ganadora en la interfaz
    """
    # Verificar filas
    for r in range(3):
        if all(board[r][c] == player for c in range(3)):
            return [(r, c) for c in range(3)]
    
    # Verificar columnas
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return [(r, c) for r in range(3)]
    
    # Verificar diagonal principal
    if all(board[i][i] == player for i in range(3)):
        return [(i, i) for i in range(3)]
    
    # Verificar diagonal secundaria
    if all(board[i][2-i] == player for i in range(3)):
        return [(i, 2-i) for i in range(3)]
    
    return []

def get_available_moves(board):
    """
    Retorna una lista de movimientos disponibles (casillas vacías)
    """
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                moves.append((r, c))
    return moves

def is_valid_move(board, row, col):
    """
    Verifica si un movimiento es válido
    """
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ""

def copy_board(board):
    """
    Crea una copia del tablero
    """
    return [row[:] for row in board]

def print_board(board):
    """
    Imprime el tablero en formato texto (útil para debug)
    """
    for row in board:
        print(" | ".join(cell if cell else " " for cell in row))
        print("-" * 9)
