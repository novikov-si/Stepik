tim = input()
rus = input()
lst = ['ножницы', 'бумага', 'камень']
if tim == rus:
    print('ничья')
else:
    kt = lst.index(tim)
    kr = lst.index(rus)
    if kt > kr:
        if kt == 2 and kr == 0:
            print('Тимур')
        else:
            print('Руслан')
    else:
        if kt == 0 and kr == 2:
            print('Руслан')
        else:
            print('Тимур')

# 2

x, y = tim, rus #input(), input()
var = ['камень', 'ножницы', 'бумага']
ans = ['ничья', 'Руслан', 'Тимур']
print(ans[var.index(x) - var.index(y)])

#3

a, b = tim, rus #input(), input()
print('ничья' if a == b else 'Тимур' if a + b in ('каменьножницы', 'бумагакамень', 'ножницыбумага') else 'Руслан')

# 4

a, b = tim, rus #input()[0], input()[0]
print('ничья' if a == b else 'Тимур' if a + b in ('кн', 'бк', 'нб') else 'Руслан')

exit()

s = ['камень', 'ножницы', 'бумага']
print(['ничья', 'Руслан', 'Тимур'][s.index(input()) - s.index(input())])

x=input()[0]+input()[0]
print((x[0]==x[1])*'ничья' or ['Тимур','Руслан'][x in 'кбнк'])
