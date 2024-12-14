import chess
board = chess.Board()
def display_board(board):
    print(board)
def get_piece_value(piece):
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0,
    }
    return values.get(piece.piece_type, 0) if piece.color == chess.WHITE else -values.get(piece.piece_type, 0)

def evaluate_board(board):
    material_count = sum(get_piece_value(piece) for piece in board.piece_map().values())
    return material_count

def generate_moves(board):
    return list(board.legal_moves)
def execute_move(board, move):
    board.push(move)
def is_game_over(board):
    return board.is_game_over()

def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in generate_moves(board):
            board.push(move)
            eval - minimax(board,depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in generate_moves(board):
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta - min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board, depth):
    best_move = None
    best_value = float('-inf')
    for move in generate_moves(board):
        board.push(move)
        move_value = minimax(board, depth - 1, float('-inf'), float('-inf'), False)
        board.pop()
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

def play_game_with_ai():
    while not is_game_over(board):
        display_board(board)
        if board.turn == chess.WHITE:
            move = input("Enter your move (e.g., e2e4): ")
            try:
                execute_move(board, chess.Move.from_uci(move))
            except ValueError:
                print("Invalid move. Try again.")
        else:
            print("AI is thinking...")
            move = best_move(board, 3)
            execute_move(board, move)
            print(f"AI plays: {move}")
    
    print("GAME OVER!")
    print(f"Result: {board.result()}")

play_game_with_ai()