string = input('Enter any string: ')

if len(string) % 2 == 0:
    string += ' '

list_string = []
for i in range(len(string)):
    list_string.append(' ')

for i in range(1, len(string)+1):
    list_string[i-1] = string[i-1]
    list_string[len(string) - i] = string[len(string) - i]
    
    for j in list_string:
        print(j, end=' ')
    print()
    

    list_string[i-1] = ' '
    list_string[len(string) - i] = ' '
