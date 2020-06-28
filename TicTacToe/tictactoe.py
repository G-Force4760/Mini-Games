board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = 'player1'
player2 = 'player2'
r = 0
w = ''
def show_board():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])
def mayx():
    while True:
        try:
            position = int(input(('{} choose a position from 1 to 9\n--> ').format(player1)).strip()) - 1
        except:
            print('Sorry but you are not able to play there.')
            continue
        if board[position] == 'X' or board[position] == 'O' or position > 8:
            print('Sorry but you are not able to play there.')
            continue
        else:
            board[position] = 'X'
            break
def mayo():
    while True:
        try:
            position = int(input(('{} choose a position from 1 to 9\n--> ').format(player2)).strip()) - 1
        except:
            print('Sorry but you are not able to play there.')
            continue
        if board[position] == 'X' or board[position] == 'O' or position > 8:
            print('Sorry but you are not able to play there.')
            continue
        else:
            board[position] = 'O'
            break
def checkrow():
    global w
    if board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]:
        if r % 2 != 0:
            w = player1
        else:
            w = player2
def checkcolumn():
    global w
    if board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8]:
        if r % 2 != 0:
            w = player1
        else:
            w = player2
def checkdia():
    global w
    if board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
        if r % 2 != 0:
            w = player1
        else:
            w = player2
def check_if_win():
    checkrow()
    checkcolumn()
    checkdia()
    return
def check_if_tie():
    global w
    if all ([board[x] != x+1 for x in range(0, 9)]) and w == '':
            w = 'tie'
def check_if_over():
    check_if_win()
    check_if_tie()
def play_game():
    show_board()
    if r % 2 != 0:
        mayx()
    else:
        mayo()
    check_if_over()
print('------Tic Tac Toe------')
player1 = input('Player One submit your name: ').strip()
player2 = input('Player Two submit your name: ').strip()
while True:
    while True:
        r = r + 1
        play_game()
        if w == player1 or w == player2 or w == 'tie':
            show_board()
            break
    if w == 'tie':
        pa = input('You had a tie.\n[1] Try again\n[2] Exit\n--> ').strip()
    elif w == player1:
        pa = input(('{} won.\n[1] Try again\n[2] Exit\n--> ').format(player1)).strip()
    elif w == player2:
        pa = input(('{} won.\n[1] Try again\n[2] Exit\n--> ').format(player2)).strip()
    if pa == 1:
        continue
    else:
        break