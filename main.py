from random import randrange


def display_board(board):
    print("""
+-------+-------+-------+
|       |       |       |
|   """, board[0][0], """   |   """, board[0][1], """   |   """, board[0][2], """   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   """, board[1][0], """   |   """, board[1][1], """   |   """, board[1][2], """   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   """, board[2][0], """   |   """, board[2][1], """   |   """, board[2][2], """   |
|       |       |       |
+-------+-------+-------+
    """, sep='')


def enter_move(board):
    move = convert_field_to_co_ordinates(int(input("Make your move: ")))
    if move in make_list_of_free_fields(board):
        board[move[0]][move[1]] = "O"
        display_board(board)
    else:
        print("Incorrect value, please try again...")
        enter_move(board)


def make_list_of_free_fields(board):
    freeFields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] != 'X') and (board[i][j] != 'O'):
                freeFields.append((i, j))
    return freeFields


def make_list_of_taken_fields(boar, sign):
    takenFields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == sign:
                takenFields.append((i, j))
    return takenFields


def victory_for(board, sign):
    takenFields = make_list_of_taken_fields(board, sign)
    if ((0, 0,) in takenFields and (1, 1,) in takenFields and (2, 2,) in takenFields) or \
            ((0, 2,) in takenFields and (1, 1,) in takenFields and (2, 0,) in takenFields):
        print("The", sign, "has won")
        return True
    for i in range(3):
        if ((i, 0,) in takenFields and (i, 1,) in takenFields and (i, 2,) in takenFields) or \
                ((0, i,) in takenFields and (1, i,) in takenFields and (2, i,) in takenFields):
            print("The", sign, "has won")
            return True
    if not make_list_of_free_fields(board):
        print("Draw")
        return True
    return False


def draw_move(board):
    freeFields = make_list_of_free_fields(board)
    if freeFields:
        move = convert_field_to_co_ordinates(randrange(8) + 1)
        while move not in freeFields:
            move = convert_field_to_co_ordinates(randrange(8) + 1)
        board[move[0]][move[1]] = "X"
        display_board(board)


def convert_field_to_co_ordinates(field):
    fieldOnBoard = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if field == fieldOnBoard:
                return i, j,
            fieldOnBoard += 1


board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

print("Tic-Tac-Toe")
display_board(board)

while True:
    enter_move(board)
    if victory_for(board, 'O'): break
    draw_move(board)
    if victory_for(board, 'X'): break
print("GAME OVER")
