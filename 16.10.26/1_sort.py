numbs = list(map(int, input().split()))
tf_num = [True] + [False] * (len(numbs) - 1)
for i in range(1, len(numbs)):
    if tf_num[i]:
        continue
    elif numbs[i] >= numbs[(i - 1) // 2]:
        tf_num[i] = True

fl = True
for el in tf_num:
    if el:
        continue
    else:
        fl = False
        break

if fl:
    print(1)
else:
    print(0)
