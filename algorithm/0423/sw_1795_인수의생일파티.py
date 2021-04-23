import sys
sys.stdin = open('sw_1795_인수의생일파티_input.txt', 'r')

from collections import deque

def dij(start, data):

    D = [987654321] * (N + 1)
    Q = deque()

    u = start
    D[u] = 0
    Q.append(u)

    while Q:
        s = Q.popleft()
        for v in range(1,N+1):
            if data[s][v] != 0 and D[v] > D[s] + data[s][v] :
                D[v] = D[s] + data[s][v]
                Q.append(v)

    return D[:]


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    arr2 = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(M):
        s, e, w = map(int,input().split())
        arr[s][e] = w
        arr2[e][s] = w

    ans = [0] * (N+1)

    ans1 = dij(X, arr)
    ans2 = dij(X, arr2)

    for i in range(1, N+1):
        ans[i] = ans1[i] + ans2[i]

    print('#{} {}'.format(tc,max(ans)))
