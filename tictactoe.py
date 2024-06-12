# Set up the game board
# Create a 2D array of 3x3 to represent the game board

current_matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
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
def game_status(x):



#Create a function to check if the game has ended in a draw.

