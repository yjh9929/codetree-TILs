N = int(input())
T = [0] * N
P = [0] * N

def dfs(n, sm):
	global ans
	# [1] 종료 조건 : 가능한 n을 종료에 관련된 것으로 정의
	if n >= N:
		ans = max(ans, sm)
		return
	# [2] 하부 함수 호출 : 화살표 개수만큼 호출 
	if n + T[n] <= N: # 외주를 받는 경우 (휴가 끝나기 전까지만 가능)
		dfs(n + T[n], sm + P[n])
	dfs (n + 1, sm) # 외주를 받지 않은 경우 (항상 바로 다음날로 가능)
for i in range(N): 
	T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)