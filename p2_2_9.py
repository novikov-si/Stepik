tim=input()
rus=input()
lst=['ножницы','бумага','камень','ящерица','Спок']
dct={'ножницы':[1,3,2,4],'бумага':[2,4,0,3],'камень':[0,3,1,4],'ящерица':[1,4,0,2],'Спок':[0,2,1,3]}
if tim==rus:
    print('ничья')
else:
    kr=lst.index(rus)
    rult=dct[tim]
    k=rult.index(kr)
    if k > 1:
        print('Руслан')
    else:
        print('Тимур')

exit()

# 2

knb = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
result_name = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
print(result_name[knb.index(input()) - knb.index(input())])

# 3

print(('ничья', *['Руслан'] * 2, *['Тимур'] * 2)[sum(i * 'Скняб'.index(input()[0]) for i in (1, -1))])

# 4

t, r = input(), input()
var = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
ans = ['ничья','Руслан', 'Тимур', 'Руслан', 'Тимур', ]
print(ans[var.index(t) - var.index(r)])


# 5

d = {'ножницы': ['бумага', 'ящерица'], 'бумага': ['камень', 'Спок'], 'камень': ['ящерица', 'ножницы'],
     'ящерица': ['Спок', 'бумага'], 'Спок': ['ножницы', 'камень']}
a, b = input(), input()
print('Тимур' if b in d[a] else 'Руслан' if a in d[b] else 'ничья')

# 6

s = list('кяСнб')
w = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']

i = s.index(input()[0]) - s.index(input()[0])

print(w[i])