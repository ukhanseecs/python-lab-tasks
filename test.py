def check_win(current_matrix):
    x_row = [0, 0, 0]
    x_col = [0, 0, 0]
    o_row = [0, 0, 0]
    o_col = [0, 0, 0]
    x_diag1 = [0, 0, 0]
    o_diag1 = [0, 0, 0]
    x_diag2 = [0, 0, 0]
    o_diag2 = [0, 0, 0]

    for i in range(0, 3):
        for j in range(0, 3):
            if current_matrix[i][j] == 'x':
                x_row[i] += 1
                x_col[j] += 1
                if i == j:
                    x_diag1[i] += 1
                if i + j == 2:
                    x_diag2[i] += 1
            elif current_matrix[i][j] == 'o':
                o_row[i] += 1
                o_col[j] += 1
                if i == j:
                    o_diag1[i] += 1
                if i + j == 2:
                    o_diag2[i] += 1

    print("x row: ", x_row)
    print("x column: ", x_col)
    print("o row: ", o_row)
    print("o column: ", o_col)
    print("x diag 1: ", x_diag1)
    print("o diag 1: ", o_diag1)
    print("x diag 2: ", x_diag2)
    print("o diag 2: ", o_diag2)


current_matrix = [['x', 'o', 'x'],
                  ['o', 'x', 'o'],
                  ['x', 'o', 'x']]

check_win(current_matrix)