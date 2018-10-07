bus_stop_count = int(input())
people_count = []
current_count = 0
for i in range(bus_stop_count):
    a, b = input().split()
    a, b = int(a), int(b)
    current_count += b - a
    people_count.append(current_count)
print(max(people_count))
