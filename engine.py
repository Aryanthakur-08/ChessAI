import chess

# Piece values used for the evaluation
pieceWeights = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

def calculateScore(board):
    """
    My custom function to see who is winning based on pieces.
    """
    if board.is_checkmate():
        # If it's White's turn and they are in checkmate, Black wins
        return -99999 if board.turn == chess.WHITE else 99999
    
    currentScore = 0
    for pieceType, value in pieceWeights.items():
        whiteCount = len(board.pieces(pieceType, chess.WHITE))
        blackCount = len(board.pieces(pieceType, chess.BLACK))
        currentScore += (whiteCount - blackCount) * value
        
    return currentScore

def miniMax(board, depth, alpha, beta, isMaximizing):
    """
    The recursive search algorithm. 
    I added Alpha-Beta pruning to make it run much faster.
    """
    if depth == 0 or board.is_game_over():
        return calculateScore(board)

    if isMaximizing:
        maxEval = -1000000
        for move in board.legal_moves:
            board.push(move)
            evalResult = miniMax(board, depth - 1, alpha, beta, False)
            board.pop()
            maxEval = max(maxEval, evalResult)
            alpha = max(alpha, evalResult)
            if beta <= alpha:
                break # Pruning the tree
        return maxEval
    else:
        minEval = 1000000
        for move in board.legal_moves:
            board.push(move)
            evalResult = miniMax(board, depth - 1, alpha, beta, True)
            board.pop()
            minEval = min(minEval, evalResult)
            beta = min(beta, evalResult)
            if beta <= alpha:
                break # Pruning the tree
        return minEval

def getAiMove(board, currentDepth):
    bestMove = None
    bestValue = -1000000
    
    for move in board.legal_moves:
        board.push(move)
        boardValue = miniMax(board, currentDepth - 1, -1000000, 1000000, False)
        board.pop()
        
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
            
    return bestMove
