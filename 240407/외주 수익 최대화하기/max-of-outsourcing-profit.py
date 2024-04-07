n = int(input())
work = []
for i in range(n):
    work.append(list(map(int, input().split())))
#print(work)
total_money = [0] * n

def solve(left_day, total_money, now):
    for a in range(left_day):
        t = work[now + a][0]
        p = work[now + a][1]
        if left_day >= t:
            total_money[now] += p
            left_day -= t
            solve(left_day - t, total_money, now)
for b in range(n):
    solve(n - b, total_money, b)
print(max(total_money))