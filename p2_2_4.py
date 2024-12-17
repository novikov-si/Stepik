lst = list(map(int, input().split()))
for i in range (1, len(lst), 2):
    lst[i - 1], lst[i] = lst[i], lst[i - 1]
print(*lst)

# 2
d = input().split()
print(d[:-1:2]) # четные позиции списка 0, 2, 4 ...
print(d[1::2]) # нечетные позиции списка 1, 3, 5 ...
d[:-1:2], d[1::2] = d[1::2], d[:-1:2] # выполнено присваивание значений списками!
print(*d)
