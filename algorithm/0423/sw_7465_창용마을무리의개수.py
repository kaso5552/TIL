import sys
sys.stdin = open('sw_7465_창용마을무리의개수_input.txt', 'r')


from collections import deque
def bfs(i):

    visited[i] = 1
    Q.append(i)

    while Q:
        s = Q.popleft()
        for v in range(1,N+1):
            if visited[v] == 0 and arr[s][v] == 1 :
                Q.append(v)
                visited[v] = 1




T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        s, e = map(int,input().split())
        arr[s][e] = 1
        arr[e][s] = 1
    ans = 0
    Q = deque()
    visited = [0] * (N+1)
    for i in range(1,N+1):
        if visited[i] == 0:
            bfs(i)
            ans += 1
    print('#{} {}'.format(tc, ans))