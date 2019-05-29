# print an input sized board 
# board has x and y position
# player moves
# win checker in all 3 directions
# also tie checker
# design
# AI


def moves(tie_sit,win_cond):
    def p1():
        try:
            player1y = int(input("PLAYER ONE select y position:  "))-1
            player1x = int(input("PLAYER ONE select x position:  "))-1
            if board[player1y][player1x]=="0":
                board[player1y][player1x]="x"
                printing_board(board)
            else:
                print("wrong placement")
                p1()
        except (ValueError,IndexError):
            print("The input you gave was wrong")
            p1()
    def p2():
        try:
            player2y = int(input("PLAYER TWO select y position:  "))-1
            player2x = int(input("PLAYER TWO select x position:  "))-1
            if board[player2y][player2x]=="0":
                board[player2y][player2x]="o"
                printing_board(board)
            else:
                print("wrong placement")
                p2()
        except (ValueError,IndexError):
            print("The input you gave was wrong")
            p2()
    while tie_sit != True and win_cond !=True:
        p1()
        tie_sit = tie(board)
        win_cond = victory_in_row(board)
        if tie_sit == True:
            print("Tie")
            break
        if win_cond == True:
            print("victory")
            break
        p2()
        tie_sit = tie(board)
        win_cond1 = victory_in_row(board)
        win_cond2 = victory_in_column(board)
       #win_cond3 = victory_in_diagonal(board)
        if tie_sit == True:
            print("Tie")
            break
        if (win_cond1 == True) or (win_cond2 == True): # or (win_cond3 == True):
            print("victory")
            break
                
def victory_in_row(board):
    for row in range(len(board)):
        for i in board:
            if ["x","x","x"] in board:
                print("X won")
                return True
            elif ["o","o","o"] in board:
                print("O won")
                return True
    return False

def victory_in_column(board):
    # for j,column in enumerate(board):
    #     for k,i in enumerate(column):
    if ((board[0][0] == "x") and (board[1][0] == "x") and (board[2][0] == "x")):
        print("victory")
        return True

def tie(x):
    for item in x:
        if "0" in item:
            return False
    print("Board is full")
    return True

def printing_board(x):
    for elem in board:
        if elem == 0:
            print("-------------")
        else:
            print("-------------")
            print("| "+" | ".join(elem)+" |")
    print("-------------")   
# size = input("size")
# block = []
# for block in range(size):

board = [["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]]#block for i in range(size)
tie_situation = None
win_condition = None
printing_board(board)
moves(tie_situation,win_condition)
