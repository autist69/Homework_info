line = str(input())
k = 2
r = 10

if len(line) <= k:
    print(ord(line[0]))
elif k < len(line) <= r:
    print(ord(line[0]) + ord(line[-1]) + ord(line[len(line) // 2]))
else:
    print(ord(line[-1]))
