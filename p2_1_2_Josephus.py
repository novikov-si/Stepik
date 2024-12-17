n, k = int(input()), int(input()) - 1
p = list(range(n))
i=0
while n > 1:
    i = (i + k) % n
    p.pop(i)
    n -= 1
print(p[0] + 1)

# 2 по формуле из вики:
def joseph(n, k):
    return 1 if n == 1 else (joseph(n - 1, k) + k - 1) % n + 1

print(joseph(int(input()), int(input())))

# 3
n, k = int(input()), int(input())
s = 0
for i in range(1, n + 1):
    s = (s + k) % i
    #print(s)
print(s + 1)
