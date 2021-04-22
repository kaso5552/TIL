import sys
sys.stdin = open('sw_5250_최소비용_input.txt', 'r')

from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dijstra(s, e):
    x, y = s, e # 시작점을 start으로 설정
    D[x][y] = 0
    Q.append((0,0))
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                temp = 1
                if arr[x][y] < arr[nx][ny]:
                    temp += arr[nx][ny] - arr[x][y]
                if D[nx][ny] > D[x][y] + temp:
                    D[nx][ny] = D[x][y] + temp
                    Q.append((nx,ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    D = [[987654321] * N for _ in range(N)]
    ans = 0
    Q = deque()
    dijstra(0, 0)
    print('#{} {}'.format(tc,D[N-1][N-1]))


#####
# dx = [0,1]
# dy = [1,0]
#
# def dijstra(s, e):
#     x, y = s, e # 시작점을 start으로 설정
#     D[x][y] = 0
#     while x != N-1 or y != N-1:
#         min = 987654321
#         for i in range(N):
#             for j in range(N):
#                 if visited[i][j] == 0 and min > D[i][j]:
#                     min = D[i][j]
#                     x, y = i, j
#         visited[x][y] = 1
#         f1 = arr[x][y]
#
#         for i in range(2):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
#                 f2 = arr[nx][ny]
#                 if visited[nx][ny] == 0:
#                     if f1 < f2 and D[nx][ny] > D[x][y] + f2 - f1 +1:
#                         D[nx][ny] = D[x][y] + f2 - f1 + 1
#                     elif f1 >= f2 and D[nx][ny] > D[x][y] + 1:
#                         D[nx][ny] = D[x][y] + 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     D = [[987654321] * N for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     ans = 0
#     dijstra(0, 0)
#     print('#{} {}'.format(tc,D[N-1][N-1]))


