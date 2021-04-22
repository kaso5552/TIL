import sys
sys.stdin = open('sw_5248_그룹나누기_input.txt', 'r')

def bfs(n):

    visited[n] = 1
    Q.append(n)

    while len(Q):
        num = Q.pop(0)
        for i in range(1, N+1):
            if visited[i] == 0 and arr[num][i] == 1:
                Q.append(i)
                visited[i] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    arr = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        s , e = data[2 * i], data[2 * i + 1]
        arr[s][e] = 1
        arr[e][s] = 1
    visited = [0] * (N+1)
    ans = 0
    Q = []
    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i)
            ans += 1
    print('#{} {}'.format(tc,ans))
