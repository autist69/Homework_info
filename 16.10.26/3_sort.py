votes = {}
n = int(input())

for i in range(n):
    name = str(input())
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

ans = dict(sorted(votes.items(), key = lambda x: (-x[1], x[0])))
print(ans)

for key, value in ans.items():
    print(f"{key}  {value}")
