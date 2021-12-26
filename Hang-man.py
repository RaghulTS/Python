# Hang Man Game
'''
_ _ _ _ _ _ _ _
|       |
|       O
|     / | \
|      / \
|
_ _ _ _ _ _ _ _

'''
print("""
************* HANGMAN *************

Be aware you can be hanged!

Rules: 

- All words are in lower Case
- You have only 7 chances
- If you enter a false letter your mistakes will be increased by 1
- If you enter a correct letter your chances remains same.

Syntax = Alphabet
Example = a

Enjoy the game!!!!
""")

import random

# a list containing questions and answer
que_ans = [
    {
    'hints': 'Hints:\n\nMost popular web browser\nAll over the world people use it.\nInteractive interface.',
    'answer': 'googlechrome'
    }, 
    {
    'hints': 'Hints:\n\nOne of the famous social media platform\nThe name has a silent meaning instant',
    'answer': 'instagram'
    },
    {
    'hints': 'Hints:\n\nOne of the oldest social media platform\nPeople from 80s kids use them.',
    'answer': 'facebook'
    },
    {
    'hints': 'Hints:\n\nA social media platform (formal)\nOfficial announcements are made',
    'answer': 'twitter'
    },
    {
    'hints': 'Hints:\n\nSocial media platform (formal)\nUsed to create profile for jobs.',
    'answer': 'linkedin'
    },
    {
    'hints': 'Hints:\n\nSocial media platform\nSend snaps for friends\nTons of camera effect.',
    'answer': 'snapchat'
    },
    {
    'hints': 'Hints:\n\nText direct messages to friends.\nAlternative for whatsapp',
    'answer': 'telegram'
    }
]

# length of the list containing questions
questions_length = len(que_ans) 
# creating a random number between 0 and length of list
ran_num = random.randint(0, questions_length-1) 


spaces = ['', '', '', '', '', '', '']


def hang_man(): # hangman
    print('_ _ _ _ _ _ _ _')
    print('|       ' + spaces[1])
    print('|       ' + spaces[2])
    print('|      ' + spaces[3] + spaces[4] + spaces[5])
    print('|      ' + spaces[6] + ' ' + spaces[0])
    print('|       ')
    print('|')
    print('_ _ _ _ _ _ _ _')


mistake = 0

false_letters = '' # letters which are not available in the answer


hint = que_ans[ran_num]['hints'] # appropriate hint from a random selected number
ans = que_ans[ran_num]['answer'] # appropriate answer from a random selected number


print('Mistakes: ' + str(mistake) + '\n')
hang_man()
print('\n' + hint)
print('\nFalse letters: ' + false_letters)

print('\n' + '_ ' * len(ans) + '\n')


# the man start to hang if mistakes increases
def man():
    if mistake == 1:
        spaces[1] = '|'
    elif mistake == 2:
        spaces[2] = 'O'
    elif mistake == 3:
        spaces[4] = '|'
    elif mistake == 4:
        spaces[3] = '/'
    elif mistake == 5:
        spaces[5] = '\\'
    elif mistake == 6:
        spaces[6] = '/'
    elif mistake == 7:
        spaces[0] = '\\'

# list contains '_' (the letter is inserted every single time)
appending_ans_list = []

for i in range(len(ans)):
    appending_ans_list.append('_')

# to find all indexes of same elements (Eg: [1, 2, 3, 4, 3, 2, 3])=>for 3=>Output:[2, 4, 6] 
def indexes(): 
    global l
    l = [] # appending the indexes
    for i in range(len(ans)):
        if ans[i] == letter:
            l.append(i)
global used
used = [] # the letters already used

# when mistake is not equal to 7
while mistake != 7: 
    letter = input('\n\n\n\n\nGive me a alphabet in lower case: ') # asks for a letter
    # if that letter is not a alphabet or it is used already or a string 
    # then it asks for input again
    while (letter in used) or (letter.isdigit()) or (len(letter)>1):
        letter = input('Give me a alphabet in lower case: ')
    # if all the conditions satisfy then the letter is appended to used[]
    used.append(letter)
    # if the letter is in the answer Eg: googlechrome
    if letter in ans:
        print('\n\nMistakes: ' + str(mistake) + '\n')
        hang_man() # printing the hang man
        print('\n' + hint)
        print('\n\nFalse letters: ' + false_letters)
        # arranging the index values to letters
        indexes()
        print('\n')
        for j in l:=
            # '_' this is replaced with letter at the correct index
            appending_ans_list[j] = letter 
        for i in appending_ans_list:
            print(i, end=' ')
            continue
    else:
        mistake += 1
        false_letters += letter
        print('\n\nMistakes: ' + str(mistake) + '\n')
        # every time mistake increases the man starts to hand
        man()
        hang_man() # printing hang man
        print('\n' + hint)
        print('\n\nFalse letters: ' + false_letters)
        print('\n')
        for i in appending_ans_list:
            print(i, end=' ')
            continue
    # game over all letters are filled
    if '_' not in appending_ans_list:
        print('\n\nYOU WIN!\n\n')
        break

# chances are over . Lose
if mistake == 7:
    print('\n\nYOU LOSE!\n\n')
    print('Correct Ans: ' + ans)

# --------Raghul
