# Set up the game board
# Create a 2D array of 3x3 to represent the game board

current_matrix = [
    ['x', 'x', 'x'],
    ['o', 0, 0],
    ['o', 0, 0]
]


# Define the player symbols (e.g., "X" and "O").
player1 = 'x'
player2 = 'o'

#Create a function to print the current state of the game board.

def current_state(current_matrix):
    print("current game board")
    print(current_matrix[0])
    print(current_matrix[1])
    print(current_matrix[2])
current_state(current_matrix)

#Create a function to check if a given move is valid (i.e., the cell is empty
# if there is zero at the place, it can be replaced
# else, not allowed

# print(current_matrix[1][2])
# i=0
# j=0   #later i and j will be user input

#if i < 3 and j < 3:

#working
def check_validity(current_matrix):
    i=int(input("row:"))
    j=int(input("column: "))
    if current_matrix[i][j]==0:
        print("valid move")
    else:
        print("inavlid move")

check_validity(current_matrix)


#else:
    #print("move is invalid")


#Create a function to check if a player has won the game.
# Maintain a count of the number of symbols for each player in each row, column, and diagonal.
# If any player has a count of 3 in a row, column, or diagonal, they have won the game.
# def game_status(x):


def get_score(current_matrix):
    #get the counnt of x's and o's in row 1
    #make a loop
    #that reads through each row
    #and counts number of x and o
    # three rows three columns two diagonals so total 8
    # two players
    # maintain 16 counts

    x_row = [0, 0, 0]
    x_col = [0, 0, 0]
    o_row = [0, 0, 0]
    o_col = [0, 0, 0]
    x_diag1 = [0, 0, 0]
    o_diag1 = [0, 0, 0]
    x_diag2 = [0, 0, 0]
    o_diag2 = [0, 0, 0]

    for i in range(0,3):
        for j in range(0,3):
            if current_matrix[i][j]=='x':
                x_row[i] += 1
                x_col[j] += 1
                if i==j:
                    x_diag1[i] +=1
                elif i+j==2:
                    x_diag2[i] +=1

            elif current_matrix[i][j]=='o':
                o_row[i] += 1
                o_col[j] += 1
                if i==j:
                    o_diag1[i] +=1
                elif i+j==2:
                    o_diag2[i] +=1


    print("x row: ", x_row)
    print("x column: ", x_col)
    print("o row: ", o_row)
    print("o column: ", o_col)
    print("x diag 1: ", x_diag1)
    print("o diag 1: ", o_diag1)
    print("x diag 2: ", x_diag2)
    print("o diag 2: ", o_diag2)




get_score(current_matrix)





