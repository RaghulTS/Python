'''
Eg 1: Input: a1b10
       Output: abbbbbbbbbb
Eg: 2: Input: b3c6d15
          Output: bbbccccccddddddddddddddd
The number varies from 1 to 99.
'''
'''
Question 2
Input: aaabbbbccee
Output: a3b4c2e2'''

# # Method 1
# string = input('Enter: ')

# num = []
# letter = []
# for i in range(len(string)):
#     if string[i].isalpha():
#         if string[i+1].isdigit() and string[i+2].isdigit():
#             num += [str(string[i+1]) + str(string[i+2])]
#             letter += [string[i]]
#         elif string[i+1].isdigit() and string[i+2].isalpha():
#             num += [string[i+1]]
#             letter += [string[i]]
#         elif string[i+2] == '':
#             num += [string[i+1]]
#             letter += [string[i]]

# for j in range(len(letter)):
#     print(str(letter[j]) * int(num[j]), end='')


# Method 2
string = input('Enter: ')
seperating_list = []
string += ' '
for i in range(len(string)-1):
    if string[i].isdigit():
        if string[i+1].isdigit():
            seperating_list.append(string[i-1:i+2])
        else:
            seperating_list.append(string[i-1:i+1])

final_seperation = []

for i in seperating_list:
    if i.isdigit():
        continue
    final_seperation.append(i)

num = []
letter = []

for element in final_seperation:
    num.append(element[1:])
    letter.append(element[:1])
    
final = []
for x in range(len(num)):
         print(int(num[x]) * str(letter[x]), end='')



'''Solution for question2'''

givStr = input('Enter: ') # aaabbddccdddl
letters = []
letters += [givStr[0]]

for i in range(len(givStr)-1):
    if givStr[i] != givStr[i+1]:
        letters += [givStr[i+1]] 

x = 0 # for list
y = 0 # for string
final = []
how_many = 0
while x != len(letters):
    try:
        if letters[x] == givStr[y]:
            y += 1
            how_many += 1
        elif letters[x] != givStr[y]:
            final += [how_many]
            x += 1
            how_many = 0
    except IndexError:
        final += [how_many]
        break


for j in range(len(letters)):
    print(letters[j] + str(final[j]), end='')
