import random
import time

def check_vertical(list):
    for i in list:
        temp = is_all_same(i)
        if temp[0]:
            return winner(*temp)

def check_horizontal(list):
    for i in zip(*list):
        temp = is_all_same(i)
        if temp[0]:
            return winner(*temp)

def check_diagonal(list):
    lt_to_rb = []
    rt_to_lb = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                lt_to_rb.append(list[i][j])
                rt_to_lb.append(list[i][-j-1])
    l = [lt_to_rb,rt_to_lb]
    for i in l:
        temp = is_all_same(i)
        if temp[0]:
            return winner(*temp)

def is_all_same(list):
    valid = ['X', 'O']
    temp = ''
    for x in range(len(list)):
        if x == 0 and list[x] in valid:
            temp = list[x]
        elif temp != list[x]:
            #print(False,'is_all_same')
            return False,temp
        if x == len(list)-1 and temp == list[x]:
           # print(True, 'is_all_same')
            return True,temp

def print_state(gameobj):
    for x in gameobj:
        for y in x:
            print(y, end=" ")
        print()
    check_vertical(gameobj)
    check_horizontal(gameobj)
    check_diagonal(gameobj)

def game_input(gameobj):
    (x,y) = tuple(map(int, input('give the cordinates with space between (ex: 1 2)').rstrip().split()))
    valid = empty_spaces(gameobj)
    global player1
    if (x,y) in valid:
        gameobj[x][y] = player1
    else:
        print('Oops, place alread occupied. Try Again')
        game_input(gameobj)

def player_identity():
    valid = ['X', 'O']
    player = input('choose a one (x) or (O):').upper()
    while player not in valid:
        print('Oops, wrong selection. Try Again')
        player = input('choose a one (x) or (O):').upper()
    print('your selection is', player, 'for player1')
    return player


def winner(T_or_F,player):
    valid = ['X', 'O']
    if T_or_F and player in valid:
        global game_not_over
        game_not_over = False
        print(player,'player win')
    
def computerplayer(gameobj):
    computer_move = random.choice(empty_spaces(gameobj))
    valid = ['X', 'O']
    global player1
    if player1 == 'X':
        cplayer = 'O'
    elif player1 == 'O':
        cplayer = 'X'
    c_input(cplayer,computer_move[0],computer_move[1])

def c_input(player,x,y):
    print('computer Turn')
    time.sleep(1)
    valid = ['X','O']
    global gameobj
    if gameobj[x][y] not in valid:
        gameobj[x][y] = player
        return True
    else:
        print('Oops, place alread occupied. Try Again')
        return False
def empty_spaces(gameobj):
    spaces = []
    for i in range(len(gameobj)):
        for j in range(len(gameobj)):
            if gameobj[i][j] == '*':
                spaces.append((i,j))
    return spaces
    
gameobj = [['*' for x in range(3)] for x in range(3)]
player1 = player_identity()
game_not_over = True
print_state(gameobj)

while game_not_over:
    game_input(gameobj)
    print_state(gameobj)
    if game_not_over:
        computerplayer(gameobj)
        print_state(gameobj)
