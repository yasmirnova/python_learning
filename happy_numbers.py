happy_nums = (4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777)
num = int(input())
for happy_num in happy_nums:
    if num % happy_num == 0:
        print('YES')
        break
else:
    print('NO')

