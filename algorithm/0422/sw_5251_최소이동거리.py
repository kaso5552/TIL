import sys
sys.stdin = open('sw_5251_최소이동거리_input.txt', 'r')

from collections import deque

def bfs():
    D[0] = 0
    Q.append(0)
    while Q:
        s = Q.popleft()
        if s == N:
            return
        for v in range(N+1):
            if data[s][v] != 0 and D[v] > D[s] + data[s][v]:
                D[v] = D[s] + data[s][v]
                Q.append(v)



T = int(input())
for tc in range(1, T+1):
    N, E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)] # s, e, w
    data = [[0] * (N+1) for _ in range(N+1)]
    D = [987654321] * (N+1)
    for s, e, w in arr:
        data[s][e] = w
    Q = deque()
    bfs()
    print('#{} {}'.format(tc,D[-1]))
