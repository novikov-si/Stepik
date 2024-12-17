print(len(max(input().split('О'))))

exit()

s = input().split('О')
print(len(max(s)))


#

exit()

# мое:

s=input()+'О'
kr=0
mr=0
for c in s:
    if c=='Р':
        kr=kr+1
    else:
        if mr < kr:
            mr=kr
        kr=0
print(mr)

# 2
