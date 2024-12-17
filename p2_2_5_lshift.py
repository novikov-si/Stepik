lst=input().split()
lst.insert(0,lst.pop())
print(*lst)

#print(lst.pop(), *lst)