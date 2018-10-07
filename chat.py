word = input()
hello = 'hello'
index = 0
for s in word:
    if index >= len(hello):
        break
    if s == hello[index]:
        index += 1
if index == len(hello):
    print('YES')
else:
    print('NO')
