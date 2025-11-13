from game_logic import print_board, check_winner, make_move
from ai_player import ai_move

def get_player_move():
    while True:
        try:
            move = int(input("Ваш ход (1-9): "))
            if 1 <= move <= 9:
                return move - 1  # конвертируем в индекс 0-8
            else:
                print("Введите число от 1 до 9.")
        except ValueError:
            print("Введите корректное число!")

def main():
    board = [" " for _ in range(9)]  # пустая доска
    player = "X"
    
    while True:
        print_board(board)
        
        if player == "X":
            move = get_player_move()
        else:
            move = ai_move(board)
            print(f"AI выбрал: {move + 1}")  # показываем игроку в привычной нумерации
        
        if make_move(board, move, player):
            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == "Ничья":
                    print("Игра закончилась ничьей!")
                else:
                    print(f"Победитель: {winner}")
                break
            # Меняем игрока
            player = "O" if player == "X" else "X"
        else:
            print("Недопустимый ход, попробуйте снова.")

if __name__ == "__main__":
    main()

