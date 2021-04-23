import sys
sys.stdin = open('sw_1249_보급로_input.txt', 'r')

from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():

    D[0][0] = 0
    Q.append((0,0))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and D[nx][ny] > D[x][y] + arr[nx][ny]:
                    D[nx][ny] = D[x][y] + arr[nx][ny]
                    Q.append((nx,ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    D = [[987654321] * (N) for _ in range(N)]
    visited = [[0] * (N) for _ in range(N)]
    Q = deque()
    bfs()
    print('#{} {}'.format(tc,D[N-1][N-1]))