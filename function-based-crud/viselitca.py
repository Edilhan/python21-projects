import random
slova=['kniga','slovo','korabl']
word=slova.randomchoice()
word1=len(word)*'*'
popytok = len(word)
t=0
while t == 0:
    print('Slovo: ',word1)
    print('popytok: ',popytok)
    bukva = input('Введи букву на латинице: ')
    if bukva in word:
        ind_bukvy= word.find(bukva) # достаем индекс найденной буквы
        i1 = ind_bukvy+1
        word1 = word1[:ind_bukvy]+bukva+word1[i1:-1] # заменяем * найденной буквой
        if word1==word:
            print('Вы выйграли')
            break

    else:
        popytok = popytok - 1
        if popytok <= 0:
            print('Вы проиграли')
            break
    
        
