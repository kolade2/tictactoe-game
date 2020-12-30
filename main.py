#tictactoe todo

# board --done
# display board -- done
# play game - done
# handle turn (make sure user inputs valid input) 
# check Win - done
  #check rows - done 
  #check columns - done 
  #check diagonals - done 
# check tie -done
#

#---------------------global variables--------------------
board =["-","-","-",
        "-","-","-",
        "-","-","-",]
game_going = True
winner = None
current_player = "X"

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])   
  print(board[6] + " | " + board[7] + " | " + board[8])

#function call to display board --> display_board()
#------------------handle_turn----------------------------
def handle_turn(current_player):

  print(current_player + "'s turn")
  position = input("choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True;
    else:
      print("You cannot go there. Try again.")

  board[position] = current_player
  display_board()
#function that controls the positioning 
#------------------flip_player----------------------------
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  else:
    current_player = "X"

#------------------handle_turn----------------------------
def check_game_over():
  check_win()
  check_tie()
#------------------handle_turn----------------------------  
def check_win():

  global winner
  #check rows 
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
    #there was a winner
  elif diagonal_winner:
      winner = diagonal_winner
  else:
    winner = None
    #there was a winner
  return

def check_rows():
  global game_going

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_going = False
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]

def check_columns():
  global game_going

  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_going = False
  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2]

def check_diagonals():
  global game_going

  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_1 or diagonal_2:
    game_going = False
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[2]
#------------------handle_turn----------------------------
def check_tie():
  global game_going

  if "-" not in board:
    game_going = False


  return
def play_game():
  #display the board
  display_board()

  while(game_going):

    handle_turn(current_player)

    check_game_over()

    flip_player()

  ##when the game ends print out wether there is a winner or not

  if winner == "X" or winner =="O":
    print(winner + " won the game ")
  else:
    winner == "None"
    print("Nobody won and It is a tie")

play_game()

