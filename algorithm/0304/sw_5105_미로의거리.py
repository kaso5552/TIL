import sys
sys.stdin = open('sw_5105_미로의거리_input.txt', 'r')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 2찾기, 출발지점 지정
def Start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def Bfs(x, y): # x, y = 탐색시작점
    Q.append((x,y))
    visited[x][y] = 1

    while len(Q) != 0: # Q가 비어있지않으면
        tx, ty = Q.pop(0) # 시작점 저장(deQueue)
        for i in range(4): # 4방향 탐색
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx < 0 or nx > N-1: continue
            if ny < 0 or ny > N-1: continue
            if visited[nx][ny] == 0 and arr[nx][ny] == 0 :
                Q.append((nx,ny))
                visited[nx][ny] = visited[tx][ty] + 1
            if arr[nx][ny] == 3:
                return visited[tx][ty] - 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    sx, sy = Start()
    visited = list([0]*N for _ in range(N))
    Q = []
    ans = Bfs(sx, sy)
    print('#{} {}'.format(tc,ans))

