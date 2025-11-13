from game_logic import make_move, check_winner

def test_make_move():
    board = [" "] * 9
    assert make_move(board, 0, "X") == True
    assert board[0] == "X"
    assert make_move(board, 0, "O") == False

def test_check_winner():
    board = ["X", "X", "X",
             " ", "O", " ",
             "O", " ", " "]
    assert check_winner(board) == "X"
