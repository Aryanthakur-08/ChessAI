import chess
import engine

def startChessMatch():
    chessBoard = chess.Board()
    print("--- CHESS ENGINE v1.0 (BYOP Submission) ---")
    print("AI starts as White. Enter moves in UCI format.")

    while not chessBoard.is_game_over():
        print("\n", chessBoard)
        
        if chessBoard.turn == chess.WHITE:
            print("\nAI is calculating...")
            aiMove = engine.getAiMove(chessBoard, 3)
            chessBoard.push(aiMove)
            print(f"AI Move played: {aiMove}")
        else:
            try:
                userMoveInput = input("\nYour move (Black): ").strip()
                if userMoveInput.lower() in ['exit', 'quit']:
                    break
                
                legalUserMove = chess.Move.from_uci(userMoveInput)
                if legalUserMove in chessBoard.legal_moves:
                    chessBoard.push(legalUserMove)
                else:
                    print("Error: Illegal move! Please try a different square.")
            except:
                print("Error: Invalid UCI format (example: e7e5).")

    print("\n--- Match Finished ---")
    print(f"Final Outcome: {chessBoard.result()}")

if __name__ == "__main__":
    startChessMatch()