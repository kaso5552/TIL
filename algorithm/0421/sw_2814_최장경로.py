import sys
sys.stdin = open('sw_2814_최장경로_input.txt', 'r')

def dfs(v):
    global ans

    visited[v] = 1

    for i in range(1, N+1):
        if visited[i] == 0 and arr[v][i] == 1:
            dfs(i)
            visited[i] = 0

    if ans < sum(visited) :
        ans = sum(visited)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        s , e = map(int,input().split())
        arr[s][e] = 1
        arr[e][s] = 1
    ans = 0
    for i in range(N):
        visited = [0] * (N + 1)
        dfs(i)
    print('#{} {}'.format(tc,ans))


