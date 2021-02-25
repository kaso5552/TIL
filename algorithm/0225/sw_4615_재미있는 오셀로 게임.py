import sys
sys.stdin = open('sw_4615_재미있는 오셀로 게임_input.txt','r')
# dx,dy 12시부터 시계방향(8방향)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def Othello(x,y,c):
    if arr[x][y] == 0:
        arr[x][y] = c
    else:
        return
    for i in range(8):
        dir = i
        count = 0
        x_loc = x
        y_loc = y
        while True:
            # 몇번 동작한지 알기 위함
            count += 1
            x_loc = x_loc + dx[dir]
            y_loc = y_loc + dy[dir]
            if 0 <= x_loc < N and 0 <= y_loc < N:
                if arr[x_loc][y_loc] == 0:
                    break
                elif arr[x_loc][y_loc] == c:
                    for i in range(count-1):
                        x_loc = x_loc - dx[dir]
                        y_loc = y_loc - dy[dir]
                        arr[x_loc][y_loc] = c
                    break
            else:
                break


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list([0] * N for _ in range(N))
    # 기본 돌 놓기
    center = N // 2
    arr[center - 1][center - 1], arr[center][center] = 2, 2  # 백
    arr[center - 1][center], arr[center][center - 1] = 1, 1  # 흑
    # 흑돌(C = 1), 백돌(C = 2)
    for i in range(M):
        Y, X, C = map(int,input().split())
        Othello(X-1, Y-1, C)
    black_count = 0
    white_count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black_count += 1
            elif arr[i][j] == 2:
                white_count += 1
    print('#{} {} {}'.format(tc,black_count,white_count))




