import sys
sys.stdin = open('sw_1263_사람네트워크2_input.txt', 'r')

from collections import deque

def bfs(start):

    u = start
    D[u] = 0
    Q.append(u)

    while Q:
        s = Q.popleft()
        for v in range(N):
            if data[s][v] == 1 and D[v] > D[s] + 1:
                D[v] = D[s] + 1
                Q.append(v)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    N = arr[0]
    data = [[0] * (N) for _ in range(N)]
    count = 1
    for i in range(N):
        for j in range(N):
            data[i][j] = arr[count]
            count += 1

    Q = deque()
    ans = [0] * N
    for i in range(N):
        D = [987654321] * N
        bfs(i)
        ans[i] = sum(D)
    print('#{} {}'.format(tc,min(ans)))