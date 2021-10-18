import sys
sys.stdin = open('sw_5653_줄기세포배양_input.txt', "r")

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(sx, sy, n, t):
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if state[nx][ny] == -9:
            state[nx][ny] = 2
            arr[nx][ny] = n
            state_check[nx][ny] = t
            Q.appendleft([nx, ny, num_state, arr[nx][ny] + t, t])
        elif state[nx][ny] == 2:
            if t == state_check[nx][ny] and arr[nx][ny] < n:
                arr[nx][ny] = n
                Q.appendleft([nx, ny, num_state, arr[nx][ny] + t, t])


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    arr = [list(0 for _ in range(600 + M)) for _ in range(600 + N)]
    state = [list(-9 for _ in range(600 + M)) for _ in range(600 + N)]
    state_check = [list(-1 for _ in range(600 + M)) for _ in range(600 + N)]
    Q = deque()
    ans = 0
    for i in range(N):
        temp = list(map(int,input().split()))
        for j in range(M):
            arr[300 + i][300 + j] = temp[j]
            if temp[j] != 0 :
                state[300 + i][300 + j] = 2
                Q.appendleft([300 + i, 300 + j, arr[300 + i][300 + j], temp[j], 0])

    while Q:
        x, y, num_state, start, k = Q.popleft()
        if k == K + 1:
            continue
        if num_state != arr[x][y]:
            continue
        num = arr[x][y]
        if state[x][y] == 2:
            if start == k:
                state[x][y] = 1
            Q.append([x, y, num_state, start, k+1])
        elif state[x][y] == 1:
            # 활성화하고
            solve(x, y, num, k)
            if arr[x][y] == k - start:
                state[x][y] = 0
            else:
                Q.append([x, y, num_state, start, k+1])
                # Q.sort(key=lambda x: x[3])

    for i in range(600 + N):
        # if state[i].count(1) or state[i].count(2):
        #     print(i, arr[i])
        ans += state[i].count(1)
        ans += state[i].count(2)

    print('#{} {}'.format(tc, ans))
