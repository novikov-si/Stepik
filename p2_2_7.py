nnum = int(input())
numlst = [int(input()) for _ in range(nnum)]
# numlst = []
# for i in range(nnum):
#    numlst.append(int(input()))
multi = int(input())

if 0 in numlst and multi == 0:
    print("ДА")
    exit()
if (1 in numlst and multi != 1 and multi in numlst
        or multi == 1 and numlst.count(1) > 1
        or multi == 1 and numlst.count(-1) > 1
        or -1 in numlst and -multi in numlst):
    print("ДА")
    exit()

numlst = [x for x in numlst if x != 1 and x != 0]

reslst = []
bno = True
for v in numlst:
    if multi % v == 0:
        reslst.append(v)

if len(reslst) > 1:
    for v in reslst:
        resw = reslst.copy()
        resw.remove(v)
        if multi // v in resw:
            print("ДА")
            bno = False
            break
if bno:
    print("НЕТ")

exit()

# 2

numbers, multiply = [int(input()) for i in range(int(input()))], int(input())
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if multiply == numbers[i] * numbers[j]:
            exit(print("ДА"))
print("НЕТ")

# 3
s, product = [int(input()) for _ in range(int(input()))], int(input())
print('ДА' if any([s[i] * j == product for i in range(len(s)) for j in s[i + 1:]]) == 1 else 'НЕТ')

# 4
*arr, n = [int(input()) for _ in range(int(input()) + 1)]
print(['НЕТ', 'ДА'][any(n / arr[i] in arr[:i] + arr[i + 1:] for i in range(len(arr)))])

# 5
from itertools import combinations

nums = [int(input()) for _ in range(int(input()))]
result = int(input())

print("ДА" if any(item[0] * item[1] == result for item in combinations(nums, 2)) else 'НЕТ')
