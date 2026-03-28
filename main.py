import chess
import engine

def printLabeledBoard(board):
    """
    This function adds rank and file labels to the board output
    so it's easier for humans to read in the terminal.
    """
    # Column headers
    print("\n     a b c d e f g h")
    print("   +-----------------+")
    
    # Split the board string into individual rows
    boardLines = str(board).split('\n')
    
    # Print each row with its rank number (8 down to 1)
    for index, line in enumerate(boardLines):
        rankNumber = 8 - index
        print(f" {rankNumber} | {line} | {rankNumber}")
        
    print("   +-----------------+")
    print("     a b c d e f g h\n")

def startChessMatch():
    chessBoard = chess.Board()
    print("--- CHESS ENGINE v1.2 (Labeled Interface) ---")
    print("AI starts as White. Use UCI format (e.g., e7e5) to play.")

    while not chessBoard.is_game_over():
        # We now use our custom labeled board instead of the basic print
        printLabeledBoard(chessBoard)
        
        if chessBoard.turn == chess.WHITE:
            print("AI is calculating...")
            # Using 'selectMove' from our humanized engine.py
            aiMove = engine.selectMove(chessBoard, 3)
            chessBoard.push(aiMove)
            print(f"AI Move: {aiMove}")
        else:
            try:
                userMoveInput = input("Your move (Black): ").strip()
                if userMoveInput.lower() in ['exit', 'quit']:
                    break
                
                legalUserMove = chess.Move.from_uci(userMoveInput)
                if legalUserMove in chessBoard.legal_moves:
                    chessBoard.push(legalUserMove)
                else:
                    print("Error: Illegal move! Check the coordinates.")
            except:
                print("Error: Invalid format. Please use UCI (like 'd7d5').")

    print("\n--- Match Finished ---")
    print(f"Final Outcome: {chessBoard.result()}")

if __name__ == "__main__":
    startChessMatch()
