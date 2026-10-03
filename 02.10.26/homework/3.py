line1, line2 = input().split()

line1 = line1[1::-1] + line1[2:]
line2 = line2[1::-1] + line2[2:]

print(f"{line1}-{line2}")
