print("Tic Tac Toe")
board=['','','','','','','','','']
def display(board):
    print()
    print(" "+board[0]+"  |  "+board[1]+"  |  "+board[2])
    print("---+----+-----")
    print(" "+board[3]+"  |  "+board[4]+"  |  "+board[5])
    print("---+----+-----")
    print(" "+board[6]+"  |  "+board[7]+"  |  "+board[8])

while True:
# --------------------------Player X---------------------------#
    display(board)
    choice = int(input("Enter a empty space for X: "))

    board[choice]="X"

    #check whether the space is occupied or not
    if board[choice] == " ":
        board[choice] = "X"
    #else:
        #print("Sorry, its already occupied")

    #check for wins
    if (board[0]=="X" and board[1]=="X" and board[2]=="X") or (board[3]=="X" and board[4]=="X" and board[5]=="X") or (board[6]=="X" and board[7]=="X" and board[8]=="X") or (board[0]=="X" and board[3]=="X" and board[6]=="X") or (board[1]=="X" and board[4]=="X" and board[7]=="X") or (board[2]=="X" and board[5]=="X" and board[8]=="X") or (board[0]=="X" and board[4]=="X" and board[8]=="X") or (board[2]=="X" and board[4]=="X" and board[6]=="X"):
        display(board)
        print("X wins")
        break
#--------------------------Player O---------------------------#
    display(board)
    choice = int(input("Enter a empty space for O: "))

    board[choice] = "O"

    # check whether the space is occupied or not
    if board[choice] == " ":
        board[choice] = "O"
    #else:
       # print("Sorry, its already occupied")

    # check for wins
    if (board[0] == "O" and board[1] == "O" and board[2] == "O") or (
            board[3] == "O" and board[4] == "O" and board[5] == "O") or (
            board[6] == "O" and board[7] == "O" and board[8] == "O") or (
            board[0] == "O" and board[3] == "O" and board[6] == "O") or (
            board[1] == "O" and board[4] == "O" and board[7] == "O") or (
            board[2] == "O" and board[5] == "O" and board[8] == "O") or (
            board[0] == "O" and board[4] == "O" and board[8] == "O") or (
            board[2] == "0" and board[4] == "O" and board[6] == "O"):
        display(board)
        print("O wins")
        break




