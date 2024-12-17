p = [0,0,0,0]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    r = x * y
    if r == 0:
        pass
    elif x > 0:
        if r > 0:
            p[0] += 1
        else:
            p[3] += 1
    else:
        if r > 0:
            p[2] += 1
        else:
            p[1] += 1
print("Первая четверть:", p[0])
print("Вторая четверть:", p[1])
print("Третья четверть:", p[2])
print("Четвертая четверть:", p[3])

# 2 ???
#{print(n, 'четверть:', q.count(i)) for q in [[((1, 0), (2, 3))[' -' in r][r[0] != '-'] for r in open(0) if '0' not in r.split()][1:]] for i, n in enumerate('Первая Вторая Третья Четвертая'.split())}