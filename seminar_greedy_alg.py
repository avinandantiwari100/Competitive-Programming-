
n = int(input("Enter number of seminars: "))

seminars = []

for i in range(n):
    start = int(input("Enter start time: "))
    end = int(input("Enter end time: "))
    seminars.append((start, end))

seminars.sort(key=lambda x: x[1])

count = 0
last_end = 0

for start, end in seminars:
    if start >= last_end:
        count += 1
        last_end = end

print("Maximum number of seminars:", count)