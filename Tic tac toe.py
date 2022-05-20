

print('****************Tic Tac Toe****************\n\nBy Raghul\n')

board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def board_function():

    # system('clear')
    
    print(board_list[0] + ' | ' + board_list[1] + ' | ' + board_list[2] + '               1 | 2 | 3')
    print('---------              -----------')
    print(board_list[3] + ' | ' + board_list[4] + ' | ' + board_list[5] + '               4 | 5 | 6')
    print('---------              -----------')    
    print(board_list[6] + ' | ' + board_list[7] + ' | ' + board_list[8] + '               7 | 8 | 9')

used_entries = [] # the entries will be inserted when used

board_function()

def the_game():
    for i in range(9):
        if i % 2 == 0: # if the player turn is even then the player is X
            print("\t\t\t--------\n \t\t\t X Turn\n\t\t\t--------")
            a = input('Enter X: ')
            if a == 'newgame':
                print('New Game !')
                break             
            while a not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                a = input('Enter x: ')
            while a in used_entries: # if the entry is used already it asks for input again
                print('This place is used already! Try Again!\n\t\t\t--------\n \t\t\t X Turn\n\t\t\t--------')
                a = input('Enter X: ')
            while a not in used_entries: # a new entry
                used_entries.append(a)
                board_list[int(a)-1] = 'X'
                board_function()
        if (board_list[0] == board_list[1] == board_list[2] == 'X') or (board_list[3] == board_list[4] == board_list[5] == 'X') or (board_list[6] == board_list[7] == board_list[8] == 'X') or (board_list[0] == board_list[3] == board_list[6] == 'X') or (board_list[1] == board_list[4] == board_list[7] == 'X') or (board_list[2] == board_list[5] == board_list[8] == 'X') or (board_list[0] == board_list[4] == board_list[8] == 'X') or (board_list[2] == board_list[4] == board_list[6] == 'X'):
            print('\n\n\t\t\t**** X Win ****\n\n')
            break
        if i % 2 != 0: # if the player turn is odd then the player is O
            print("\t\t\t--------\n \t\t\t O Turn\n\t\t\t--------")
            b = input("Enter O: ")
            if b == 'newgame':
                print('New Game !')
                break
            while b not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                b = input('Enter O: ')     
            while b in used_entries: # if the entry is used already it asks for input again
                print('This place is used already! Try Again!\n--------\n \t\t\t O Turn\n\t\t\t--------')
                b = input('Enter O: ')
            while b not in used_entries: # a new entry
                used_entries.append(b)
                board_list[int(b)-1] = 'O'
                board_function()
        if (board_list[0] == board_list[1] == board_list[2] == 'O') or (board_list[3] == board_list[4] == board_list[5] == 'O') or (board_list[6] == board_list[7] == board_list[8] == 'O') or (board_list[0] == board_list[3] == board_list[6] == 'O') or (board_list[1] == board_list[4] == board_list[7] == 'O') or (board_list[2] == board_list[5] == board_list[8] == 'O') or (board_list[0] == board_list[4] == board_list[8] == 'O') or (board_list[2] == board_list[4] == board_list[6] == 'O'):
            print('\n\n\t\t\t**** O Win ****\n\n')
            break
    else:
        print('Draw Match!')
    global play_again
    play_again = input('Do You Want To Play Again (y/n) ? ')

the_game()


while play_again == 'y':
    
    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    used_entries.clear()
    board_function()
    the_game()

else:
    print('Bye Bye !')

    

# Method two    
    
pos_val = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def print_board():
    print(pos_val[0] + " | " + pos_val[1] + " | " + pos_val[2])
    print("----------")
    print(pos_val[3] + " | " + pos_val[4] + " | " + pos_val[5])
    print("----------")
    print(pos_val[6] + " | " + pos_val[7] + " | " + pos_val[8])

print_board()

def win_case(a):
    global flag
    flag = False
    if (pos_val[0] == pos_val[1] == pos_val[2] == a):
        flag = True
    elif (pos_val[3] == pos_val[4] == pos_val[5] == a):
        flag = True
    elif (pos_val[6] == pos_val[7] == pos_val[8] == a):
        flag = True
    elif (pos_val[0] == pos_val[4] == pos_val[8] == a):
        flag = True
    elif (pos_val[6] == pos_val[4] == pos_val[2] == a):
        flag = True
    elif (pos_val[0] == pos_val[3] == pos_val[6] == a):
        flag = True
    elif (pos_val[1] == pos_val[4] == pos_val[7] == a):
        flag = True
    elif (pos_val[2] == pos_val[5] == pos_val[8] == a):
        flag = True



while True:
    x = (input("Enter place for x: "))

    while (x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        print("Invalid")
        x = (input("Enter place for x: "))

        
    
    while (pos_val[int(x)-1] == "x" or pos_val[int(x)-1] == "o"):
        print("Invalid")
        x = (input("Enter place for x: "))
        
    pos_val[int(x)-1] = "x"
    print_board()
    winning = "x"
    win_case(winning)

    if (flag == True):
        print(winning , "won")
        break
    
    o = (input("Enter place for o: "))

    while (o not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        print("Invalid")
        o = (input("Enter place for x: "))

    
    
    while (pos_val[int(o)-1] == "x" or pos_val[int(o)-1] == "o"):
        print("Invalid")
        o = (input("Enter place for o: "))
    
    pos_val[int(o)-1] = "o"
    print_board()

    winning = "o"
    win_case(winning)
    
    if (flag == True):
        print(winning , "won")
        break

        

