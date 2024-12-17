lst = list(map(int, input().split()))
res = 0
prev = lst[0]
for val in lst:
    if val > prev:
        res += 1
    prev = val
print(res)

# 2
nums = tuple(map(int, input().split()))
print(sum(1 for i in range(1, len(nums)) if nums[i - 1] < nums[i]))
# 3
print(sum(nums[i - 1] < nums[i] for i in range(1, len(nums))))
