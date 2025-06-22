# ai.py - Tic Tac Toe AI logic

def get_ai_move(board, ai_symbol, player_symbol):
    """
    Returns the best move for the AI as (row, col).
    Uses a simple minimax algorithm for unbeatable AI.
    """
    best_score = -float('inf')
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                board[r][c] = ai_symbol
                score = minimax(board, 0, False, ai_symbol, player_symbol)
                board[r][c] = ''
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move

def minimax(board, depth, is_maximizing, ai_symbol, player_symbol):
    from src.game_logic.game_logic import check_winner, is_draw
    if check_winner(board, ai_symbol):
        return 10 - depth
    if check_winner(board, player_symbol):
        return depth - 10
    if is_draw(board):
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '':
                    board[r][c] = ai_symbol
                    score = minimax(board, depth+1, False, ai_symbol, player_symbol)
                    board[r][c] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '':
                    board[r][c] = player_symbol
                    score = minimax(board, depth+1, True, ai_symbol, player_symbol)
                    board[r][c] = ''
                    best_score = min(score, best_score)
        return best_score
