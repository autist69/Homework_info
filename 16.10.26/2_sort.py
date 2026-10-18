french = set(map(int, input().split()))
swim = set(map(int, input().split()))
piano = set(map(int, input().split()))

ans = list(swim & piano - french)
ans.sort()

print(*ans)
