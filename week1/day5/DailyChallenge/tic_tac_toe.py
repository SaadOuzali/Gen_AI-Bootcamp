
board: list = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
winner: str = None
pl_inp: dict = {}
kepp_game_run: bool = True
total_board_position: bool = True
game_start: bool = True
player_1: dict = {}
player_2: dict = {}
current_player: dict = {}


# to print the board game
def print_board():
    print("welcom to tic tac toe game ! \n")
    print("TIC TAC TOE \n")
    print("******** ")
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|" + board[i][j], end="")
        print("|")
        print("********")


# to take value from the user (row, col and symbol)
def player_draw_board_ipnut(current_player_name:str) -> dict:
    player_input_row = int(input(f"{current_player_name} enter the row position : "))
    player_input_col = int(input(f"{current_player_name} enter the col position : "))
    player_input_X_or_O = input(f"{current_player_name} enter a symbol  (‘O’ or ‘X’) ")
    pl_input = {
        "row": player_input_row,
        "col": player_input_col,
        "sym": player_input_X_or_O,
    }
    return pl_input


# to define the position of the symbol in the board
def player_input(player: dict):
    row = player["row"] if 0 <= player["row"] <= 2 else None
    col = player["col"] if 0 <= player["row"] <= 2 else None
    if row or col or board[row][col] == "-":
        board[row][col] = player["sym"]
        print_board()
    else:
        print("malk barhoch asa7bi l3ab ola sir f7alk .")





# to check the winner in the horizontal on the board
def checkhorizontal(board: list) -> bool:
    global winner
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != "-":
        winner = board[0][0]
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != "-":
        winner = board[0][1]
        return  True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != "-":
        winner = board[2][0]
        return True
    else:
        return False


# to check the winner in the vertical on the board
def checkvertical(board: list) -> bool:
    global winner
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != "-":
        winner = board[0][0]
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != "-":
        winner = board[0][1]
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != "-":
        winner = board[2][0]
        return True
    else:
        return False


# to check the winner in the diagonal on the board
def checkdiagonal(board: list) -> bool:
    global winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        winner = board[0][0]
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        winner = board[0][1]
        return True
    else:
        return False


def check_if_win(board: list):
    global kepp_game_run,winner

    check_row = checkhorizontal(board=board)
    check_col = checkvertical(board=board)
    check_diag = checkdiagonal(board=board)

    if check_row or check_col or check_diag:
        kepp_game_run = False
        print("rab7 hna")       
        return {"winner": True, "state": "win"}
    else:
        print("marab7ch hna")
        return {"winner": False, "state": "ongoing"}


# check if the result is tie
def check_for_tie(board: list) -> dict:
    global kepp_game_run
    check_winner = check_if_win(board=board)
    if check_winner["state"] == "ongoing" and not any(
        cell == "-" in row for row in board for cell in row
    ):
        print("slat ta3adol")
        kepp_game_run = False
        return  {"winner": False, "state": "tie"}
    else:
       print("ba9i ta7d marba7")
       return check_winner




def prompt_template(template: str):
    while True:
        inp = input(template)
        if inp:
            return inp
        print("zair m3ana lai7fdk ")


def choice_symbole(player: dict):
    name=player["name"]
    while True:
        sym =  input(f"{name} please choice symbol (‘O’ or ‘X’)  :").strip().upper()
    
        if sym in {"O", "X"}:
            player["symbol"] = sym
            return player["symbol"]
        else:
            print("invalid symbol please try again choice between (‘O’ or ‘X’)")


def choice_player_name_and_symbol():

    player_1["name"] = prompt_template("enter player 1 name : ")
    player_2["name"] = prompt_template("enter player 2 name : ")

    if player_1["name"] != player_2["name"] :
        player_1["symbol"] = choice_symbole(player=player_1)
        player_2["symbol"] = "X" if player_1["symbol"] == "O" else "O"
        return (player_1, player_2)


def play(board: list):
    global current_player, kepp_game_run,winner
    print_board()
    player_1, player_2 = choice_player_name_and_symbol()
    name=player_1["name"]
    print(f"{name} start the game please")
    current_player = player_1

    while kepp_game_run:
        player = player_draw_board_ipnut(current_player_name=current_player["name"])
        sym=player["sym"]
        print(f"player sym {sym}")
        print(f"player sym {current_player}")
        print(current_player["symbol"])
        if player["sym"] == current_player["symbol"]:
            player_input(player=player)
            check_res=check_for_tie(board=board)
            if check_res["state"]=="ongoing":
                current_player=player_2 if current_player["name"] ==player_1["name"]  else player_1
            elif check_res["state"]=="win" :
                print(f"congratulation the winner is {winner}")
                
            else:
                pass


play(board=board)






