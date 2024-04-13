N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N//2
ans = 100 * M * M # 걍 좀 큰 숫자로 정의함

def dfs(n, alst, blst):
    global ans

    if n == N: # 이때 정답을 처리하게 되는 거임
        if len(alst)==len(blst):    # 같은 인원수로 팀을 구성
            asm = bsm = 0 # cal 함수로 빼면 시간이 더 오래 걸림
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asm - bsm)) # abs 절대값
        return

    dfs(n+1, alst+[n], blst)    # 오전 선택
    dfs(n+1, alst, blst+[n])    # 오후 선택


dfs(0, [], [])
print(ans)