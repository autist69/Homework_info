line = str(input())
length = len(line)
k = 4

if length >= k:
    if (line[:3] == line[:3].upper() or line[1:4] == line[1:4].upper() or
    line[0] + line[2:4] == (line[0] + line[2:4]).upper() or
    line[3] + line[:2] == (line[1] + line[:2]).upper()):
        print(line.upper())
elif line != line.upper():
        print(line)
