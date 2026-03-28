import chess


Pawn = chess.PAWN
Knight = chess.KNIGHT
Bishop = chess.BISHOP
Rook = chess.ROOK
Queen = chess.QUEEN
King = chess.KING


pieceValues = {
    Pawn: 100,
    Knight: 320,
    Bishop: 330,
    Rook: 500,
    Queen: 900,
    King: 20000
}

def getPositionRating(board):
    """
    This function looks at the board and gives a score.
    Positive score = White is winning.
    Negative score = Black is winning.
    """
    if board.is_checkmate():
        # If it's White's turn and they are in mate, Black wins (-1M)
        if board.turn == chess.WHITE:
            return -1000000
        else:
            return 1000000
            
    currentScore = 0
    # Loop through each piece type and tally up the material
    for pieceType, value in pieceValues.items():
        whiteCount = len(board.pieces(pieceType, chess.WHITE))
        blackCount = len(board.pieces(pieceType, chess.BLACK))
        currentScore += (whiteCount - blackCount) * value
        
    return currentScore

def runSearch(board, depth, alpha, beta, isMaximizing):
    """
    The main Minimax algorithm with Alpha-Beta pruning.
    It recursively checks future moves to find the best path.
    """
    if depth == 0 or board.is_game_over():
        return getPositionRating(board)

    if isMaximizing:
        bestScore = -1000000
        for move in board.legal_moves:
            board.push(move)
            evalResult = runSearch(board, depth - 1, alpha, beta, False)
            board.pop()
            
            # Updating the best score and the alpha threshold
            bestScore = max(bestScore, evalResult)
            alpha = max(alpha, evalResult)
            
            # Pruning: stop searching this branch if it's already worse
            if beta <= alpha:
                break 
        return bestScore
    
    else:
        bestScore = 1000000
        for move in board.legal_moves:
            board.push(move)
            evalResult = runSearch(board, depth - 1, alpha, beta, True)
            board.pop()
            
            # Updating the best score and the beta threshold
            bestScore = min(bestScore, evalResult)
            beta = min(beta, evalResult)
            
            # Pruning logic
            if beta <= alpha:
                break 
        return bestScore

def selectMove(board, currentDepth):
    """
    This is the entry point called by main.py.
    It picks the move that has the highest 'runSearch' score.
    """
    bestMoveFound = None
    highestValue = -1000000
    
    for move in board.legal_moves:
        board.push(move)
        # We start the recursive search one level deeper
        moveValue = runSearch(board, currentDepth - 1, -1000000, 1000000, False)
        board.pop()
        
        if moveValue > highestValue:
            highestValue = moveValue
            bestMoveFound = move
            
    return bestMoveFound
