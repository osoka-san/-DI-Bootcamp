import os

def display_board(spots):
    board = (
        f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
        f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
        f"|{spots[7]}|{spots[8]}|{spots[9]}|"
    )
    print(board)

def check_turn(turn):
    return 'O' if turn % 2 == 0 else 'X'

def check_win(spots):

    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # горизонтали
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # вертикали
        (1, 5, 9), (3, 5, 7)              # диагонали
    ]
    for a, b, c in win_conditions:
        if spots[a] == spots[b] == spots[c]:
            return True
    return False

def player_input(player):
    while True:
        choice = input(f"Player {player}'s turn: Pick your spot or press q to quit: ")
        if choice == 'q':
            return choice
        if choice.isdigit() and int(choice) in range(1, 10):
            return int(choice)
        print("Invalid input, please try again.")

def play():
    spots = {i: str(i) for i in range(1, 10)}
    playing = True
    turn = 0
    
    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(spots)
        
        player = (turn % 2) + 1
        choice = player_input(player)
        
        if choice == 'q':
            playing = False
            break
        
        if spots[choice] not in {'X', 'O'}:
            spots[choice] = check_turn(turn + 1)
            turn += 1
        else:
            print("Spot already taken, please pick another.")
            continue
        
        if check_win(spots):
            playing = False
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(spots)
            print(f"Player {player} Wins!")
            return
        
        if turn == 9:
            playing = False
            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(spots)
            print("It's a tie!")
            return

    print("Thanks for playing!")

