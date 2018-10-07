input()
s = input().split()
group_count = {'1': 0, '2': 0, '3': 0, '4': 0}
for i in s:
    group_count[i] += 1
taxi_count = group_count['4'] + group_count['3'] + group_count['2'] // 2
remaining = 0
if group_count['2'] % 2 != 0:
	remaining += 2
if group_count['3'] < group_count['1']:
	remaining += group_count['1'] - group_count['3']
taxi_count += remaining // 4 + (0 if remaining % 4 == 0 else 1)
print(taxi_count)
