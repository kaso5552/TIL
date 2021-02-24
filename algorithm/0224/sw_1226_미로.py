import sys
sys.stdin = open('sw_1226_미로_input.txt', 'r')
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def Find(x, y):
    arr[x][y] = 1
    for i in range(4):
        dir = i
        x += dx[dir]
        y += dy[dir]
        if arr[x][y] == 0:
            Find(x, y)
        elif arr[x][y] == 3:
            result.append(1)
            break
        x -= dx[dir]
        y -= dy[dir]


T = 10
for tc in range(1,T+1):
    test = int(input())
    arr = list(list(map(int,input())) for _ in range(16))
    stack = []
    result = []
    Find(1, 1)
    ans = 0
    if len(result) > 0:
        ans = 1
    print('#{} {}'.format(tc,ans))
