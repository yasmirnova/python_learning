_, k = input().split()
k = int(k)
line = input()
nums = []
for s in line.split():
    nums.append(int(s))
min_num = nums[k - 1]
counter = 0
for n in nums:
    if n == 0 or n < min_num:
        break
    counter += 1
print(counter)
