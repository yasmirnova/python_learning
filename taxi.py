n = input()
s = input().split()
student_count = {'1': 0, '2': 0, '3': 0, '4': 0}
for i in s:
    student_count[i] +=1
taxi_num = student_count['4'] + student_count['2'] // 2
student_count['2'] = 0 if student_count['2'] % 2 == 0 else 1
if student_count['3'] < student_count['1']:
    taxi_num += student_count['3']
    student_count['1'] -= student_count['3']
    taxi_num += (student_count['1'] + 2 * student_count['2']) // 4
    taxi_num += 0 if (student_count['1'] + 2 * student_count['2']) % 4 == 0 else 1
elif student_count['3'] > student_count['1']:
    taxi_num += student_count['1']
    student_count['3'] -= student_count['1']
    taxi_num += student_count['3'] + student_count['2']
else:
    taxi_num += student_count['3'] + student_count['2']
print(taxi_num)
