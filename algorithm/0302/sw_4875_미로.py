import sys
sys.stdin = open('sw_4875_미로_input.txt','r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def Dfs(x, y):
    global ans
    if data[x][y] == 3:
        ans = 1
        return
    elif data[x][y] == 0:
        data[x][y] = 1
        dir = 0
        for i in range(4):
            x_loc = x + dx[dir]
            y_loc = y + dy[dir]
            dir += 1
            if 0 <= x_loc < N and 0 <= y_loc < N:
                if data[x_loc][y_loc] != 1:
                    Dfs(x_loc, y_loc)
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(list(map(int, input())) for _ in range(N))
    ans = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                data[i][j] = 0
                Dfs(i, j)
                break
    print('#{} {}'.format(tc, ans))