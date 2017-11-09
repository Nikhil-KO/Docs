#fully functional secret santa script by AladeenIII
from random import shuffle
print(" welcome to the secret santa programm... \n use only lower case \n to start, type a name and press <enter> \n")
names = []
names.append(input())
x = True
while x == True:
    y = input("\nAdd another user and press <enter> or type 'end' and press <enter> to stop \n\n")
    if y == "end" or y == "'end'":
        print('\n' + str(names))
        print('\nOk the names above ^ are ready and will be shuffled! \nPlease come to the computer in order of names input to find out who your target is\n')
        x = False
    elif y == '':
        print()
    else:
        names.append(y)
        
santa_list = names.copy()
shuffle(santa_list)
for i in range(0,len(names)):
    person = names[i]
    santa = 'fail'
    for i in range(0,len(santa_list)):
        if person == santa_list[i]:
            w = (i+1)%(len(santa_list))
            santa = santa_list[w]
    print('\n'*100) 
    print(person + " press <enter> to know your secret santa")
    next_line = input("")
    print("your target is " + santa + '\n')
    print(person + " press <enter> before passing it on")
    next_line = input("")
    print('\n'*100) #a better way is to clear console, but dont know how yet
print('gg wp')




    
