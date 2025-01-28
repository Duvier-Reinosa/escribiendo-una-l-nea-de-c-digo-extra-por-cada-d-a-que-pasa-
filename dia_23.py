board = [' '] * 9
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]}|{board[i+1]}|{board[i+2]}")
        if i < 6: print("-+-+-")
def check_winner():
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ' or board[i*3] == board[i*3+1] == board[i*3+2] != ' ': return True
    return board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' '
def play():
    turn = 'X'
    for _ in range(9):
        print_board()
        pos = int(input(f"Turno {turn}, elige posición (0-8): "))
        if board[pos] == ' ':
            board[pos] = turn
            if check_winner():
                (print_board(), print(f"¡{turn} gana!"))
                return
            turn = 'O' if turn == 'X' else 'X'
        else: print("Posición ocupada, intenta otra.")
    (print_board(), print("¡Es un empate!"))
play()