text = str(input())
inf = text.split("student_")
inf_dict = {}

for points in inf:
    if points != "":
        inf_dict[points[:3]] = int(points[3:])

maxpoints = max(list(inf_dict.values()))

fl = 0
for number in inf_dict.items():
    if number[1] == maxpoints:
        if fl:
            print(f"-{number[0]}", end="")
        else:
            print(number[0], end="")
            fl = 1
