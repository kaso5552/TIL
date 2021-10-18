import sys
sys.stdin = open('sw_5650_핀볼게임_input.txt', 'r')

dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]
change = [0, 3, 4, 1, 2]
block = [0, [0, 3, 1, 4, 2], [0, 4,3,1,2], [0, 2,4,1,3], [0, 3,4,2,1]]
def game(x, y, d):
    nx, ny = x, y
    sx, sy = x, y
    result = 0
    while True:
        nx += dx[d]
        ny += dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            temp = arr[nx][ny]
            if temp == -1:
                break
            elif nx == sx and ny == sy:
                break
            elif temp == 0:
                continue
            elif 0 < temp < 5:
                result += 1
                d = block[temp][d]
            elif temp == 5:
                result += 1
                d = change[d]
            else:
                x1, y1 = holl[temp][0]
                x2, y2 = holl[temp][1]
                if nx == x1 and ny == y1:
                    nx, ny = x2, y2
                else:
                    nx, ny = x1, y1
        else:
            result += 1
            d = change[d]
            if nx == sx and ny == sy:
                break
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    holl = [[] for _ in range(11)]
    ans = 0
    # holl check
    for x in range(N):
        for y in range(N):
            if 6 <= arr[x][y] <= 10:
                holl[arr[x][y]].append([x,y])

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                for k in range(1,5):
                    temp = game(x, y, k)
                    if ans < temp:
                        ans = temp

    print('#{} {}'.format(tc, ans))

