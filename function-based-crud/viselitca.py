import random
slova=('kniga','slovo','korabl')
word=random.choice(slova)
word1=len(word)*'*'
popytok = len(word)
t=0
while t == 0:
    print('Слово: ',word1)
    print('Осталось попыток: ',popytok)
    bukva = input('Введи букву на латинице, translit epta: ')
    if bukva in word:
        ww=''
        for i in range(len(word)):
            if bukva == word[i]:
                ww = ww+bukva
            else:
                ww = ww + word1[i]
        word1 = ww

            
        # ind_bukvy= word.find(bukva) # достаем индекс найденной буквы
        # i1 = ind_bukvy+1
        # word1 = word1[:ind_bukvy]+bukva+word1[i1:-1] # заменяем * найденной буквой
        if word1==word:
            print('Вы выйграли, загаданное слово:', word)
            break

    else:
        popytok = popytok - 1
        if popytok <= 0:
            print('Вы проиграли, перезапусти прогу чтобы попытаться заново')
            break
    
        
