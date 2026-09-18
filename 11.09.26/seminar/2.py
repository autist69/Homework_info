inf = list(map(str, input().split())); n = int(inf[0]); k = -1
for i in range(len(inf[1]) // n):
    if k > -1:
        print(inf[1][k + n : k : -1], end = ""); k += n
    else:
        print(inf[1][k + n :: -1], end = ""); k += n