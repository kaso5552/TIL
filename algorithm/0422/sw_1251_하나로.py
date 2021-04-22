import sys
sys.stdin = open('sw_1251_하나로_input.txt', 'r')

def prim():
    total = 0
    u = 0
    D[0] = 0
    for i in range(N):
        min = 999999999999
        for v in range(N):
            if visited[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visited[u] = 1
        total += data[PI[u]][u]

        for v in range(N):
            if visited[v] == 0 and D[v] > data[u][v]:
                D[v] = data[u][v]
                PI[v] = u
    return total

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_data = list(map(int,input().split()))
    y_data = list(map(int,input().split()))
    E = float(input())
    data = [[0] * N for _ in range(N)]
    for s in range(N):
        for e in range(s, N):
            data[s][e] = ((x_data[s] - x_data[e]) ** 2 + (y_data[s] - y_data[e]) ** 2) * E
            data[e][s] = data[s][e]
    D = [999999999999] * N
    visited = [0] * N
    PI = list(range(N))

    print('#%d %d'%(tc,round(prim())))