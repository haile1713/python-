board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

user =True
turns =0

def print_board(board):
    for row in board:
        for slot in row:
            print(slot + " ", end="")
        print()

def quit_game(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing")
        return True
    else:
        return False

def check_input(user_input):
    if not user_input.isnumeric():
        print("Invalid input, please enter a number from 1 to 9")
        return False

    user_input = int(user_input)
    if not 1 <= user_input <= 9:
        print("Number out of range, please enter a number from 1 to 9")
        return False

    return True

def is_taken(coords, board):
    row, col = coords
    if board[row][col] != "-":
        print("Position already taken, please choose another")
        return True
    else:
        return False

def get_coordinates(user_input):
    user_input = int(user_input) - 1
    row = user_input // 3
    col = user_input % 3
    return row, col

def add_to_board(coords, board,active_user):
    row, col = coords
    board[row][col] = active_user

def current_user(user):
    if user:
        return "x"
    else :
        return "O"

def iswin(user,board):

    if check_row(user,board):   
         return True   
    if check_col (user,board):
        return True
    if check_diag (user,board):
        return True
    return False
def check_row(user,board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row : return True
    return False


def check_col(user,board):
    
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if  complete_col : return True
    return False 


def check_diag(user,board):
    if board [0][0] == user and  board [1][1] == user and board[2][2] ==user:
        return True
    elif board[0][2] == user and board [1][1] ==user and board [2][0] == user:
        return True
    else: return False

while turns <9 :
    active_user=current_user(user)
    print_board(board)
    user_input = input("Enter a position 1-9, or enter 'q' to quit: ")
    if quit_game(user_input):
        break
    if not check_input(user_input):
        continue
    row, col = get_coordinates(user_input)
    if is_taken((row, col), board):
        continue
    add_to_board((row, col), board,active_user)

    if iswin(active_user,board):
        print (f"{active_user.upper()} Won!")
        break
    turns +=1
    if turn ==9 :
        print ("draw!")
    user= not user
