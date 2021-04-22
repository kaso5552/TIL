import sys
sys.stdin = open('sw_5249_최소신장트리_input.txt', 'r')

def prim():
    u = 0
    D[u] = 0
    ans = 0

    for i in range(V+1):
        min = 987654321
        for v in range(V+1):
            if visited[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visited[u] = 1
        ans += min

        for v in range(V+1):
            if adj[u][v] != 0 and visited[v] == 0 and D[v] > adj[u][v]:
                D[v] = adj[u][v]

    return ans
T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]

    D = [987654321] * (V+1)
    visited = [0] * (V+1)

    # 입력
    for i in range(E):
        edge = list(map(int, input().split()))
        adj[edge[0]][edge[1]] = edge[2]
        adj[edge[1]][edge[0]] = edge[2]

    print('#{} {}'.format(tc,prim()))