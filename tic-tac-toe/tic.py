board =[
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

# print(board)

def print_board(board):
    for row in board:
        for slot in row :
            print(slot + " " , end="")
        print()

# print_board(board)

def quit(user_quit):

    if user_input.lower() =="q":
        print("thanks for playing")
        return True
    else:
        return False


def check_input(user_input):
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    
    if not check_1_9(user_input): return False
    return True
def check_1_9(user_input):
    if user_input >9 or user_input <1:
        print ("number out of range")
        return False


    else:
        return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("Invalid input ") 
        return False
    else:
        return True

def istaken(coords,board):
    row = coords[0]
    col = coords[1]

    if board[row][col] != "-":
        print("position taken")
        return True
    else :
        return False

def coordinates(user_input):
    row = int(user_input/3)
    col= user_input
    if col >2 :
        col=int(col%3)
    return (row,col)

def add_to_board(coords,board):
    row =coords[0] 
    col = coords[1]

    board[row][col] = "x"

while True:
    print_board(board)
    user_input=input("Enter a position 1-9: or enter \"q\" to quit:")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("try again")
        continue
    user_input= int(user_input)-1
    coords=coordinates(user_input)
    # board[0][0]="x"
    if istaken (coords,board):
        print (" try again")
        continue
    