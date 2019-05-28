# print an input sized board 
# board has x and y position
# player moves
# win checker in all 3 directions
# also tie checker
# design
# AI


def moves():
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
        except ValueError:
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
        except ValueError:
            print("The input you gave was wrong")
            p2()
    while Win_condition is False:
        p1()
        p2()
        
                
# def victory(x):
#     def victory_in_row(x):
        
#     # def victory_in_column():
#     # def victory_in_diagonal():

#     # victory_row = False
#     # victory_column = False
#     # victory_diagonal = False
#     # victory_in_row()
#     # victory_in_column()
#     # victory_in_diagonal()       

def printing_board(x):
    for elem in board:
        print(" | ".join(elem))

        
            

block = []
board = []#block for i in range(size)

size = int(input("gimme a size: "))   
for sor in range (size):
    block.append("0")
    board.append(block)
    board.append("-"*size)
    


#[["0","0","0"],["0","0","0"],["0","0","0"]]#
Win_condition = False

printing_board(board)

moves()
#victory(board)


