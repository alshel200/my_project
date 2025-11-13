def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(f" {row} ")
        if i < 2:
            print("---+---+---")
    print("\n")


def make_move(board, position, player):
    if 0 <= position < 9 and board[position] == " ":
        board[position] = player
        return True
    return False

def check_winner(board):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  # строки
        [0,3,6],[1,4,7],[2,5,8],  # столбцы
        [0,4,8],[2,4,6]           # диагонали
    ]
    for line in win_conditions:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]
    if " " not in board:
        return "Ничья"
    return None
