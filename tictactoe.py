# Description: A simple tic-tac-toe game.

current_matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

player1 = 'player 1 (x)'
player2 = 'player 2 (o)'

def current_state(matrix):
    print("current game board")
    for row in matrix:
        print(row)

current_state(current_matrix)

game_exit = False

def check_win(matrix):
    global game_exit

    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] !=0:
            print(f'{matrix[i][0]} wins''')
            game_exit = True
            return
        if matrix[0][i] == matrix[1][i] == matrix[2][i] !=0:
            print(f'{matrix[0][i]} wins''')
            game_exit = True
            return


    if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
        print(f"{matrix[0][0]} wins!")
        game_exit = True
        return
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
        print(f"{matrix[0][2]} wins!")
        game_exit = True
        return



def check_draw(current_matrix):
    global game_exit

    filled_square=0
    for i in range(0,3):
        for j in range(0,3):
            if current_matrix[i][j] != 0:
                filled_square +=1
            if filled_square == 9:
                game_exit = True


def game_loop(x):
    global game_exit
    current_player = player1
    filled_square = 0
    while not game_exit:
        current_state(current_matrix)
        print(f"{current_player}, it's your turn.")
        try:
            i=int(input("row number (0-2): "))
            j=int(input("column number (0-2): "))
            if current_matrix[i][j] == 0:
                if current_player == player1:
                    current_matrix[i][j] = 'x'
                    filled_square += 1

                elif current_player== player2:
                    current_matrix[i][j] = 'o'
                    filled_square +=1

                # turn switching
                if current_player == player1:
                    current_player = player2
                elif current_player == player2:
                    current_player = player1
            else:
                print("ERROR!")
                print("choose some other box")

        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

        current_state(current_matrix)
        check_win(current_matrix)
        check_draw(current_matrix)
        if game_exit == True:
            print("GAME OVER")


game_loop(current_matrix)




