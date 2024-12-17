
# Standard American Convention

#s="{:,}".format(int(input()))

num = input()

if num.isdecimal():

    s="{:,}".format(int(num))
    print(s)

    # +1
    print(f'{int(num):,}')

    # +5
    print(format(int(num), ","))

num = num + 'aaa'

### n = list(input()) список из сьроки

# +3 рекурсия (и не только цифры)
def comma(st):
    if len(st) < 4:
        return st
    return comma(st[:-3]) + ',' + st[-3:]

print(comma(num))

# +4
a = num[: : -1]
print(",".join([a[ i: i + 3] for i in range(0, len(a), 3)])[ : : -1])

# +2 использование RANGE с шагом -3, начиная с последней позиции запятой
for idx in range(len(num) - 3, 0, -3):
    num = num[:idx] + ',' + num[idx:]
print(num)




