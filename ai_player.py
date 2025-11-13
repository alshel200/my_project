import random

def ai_move(board):
    empty_positions = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(empty_positions)
