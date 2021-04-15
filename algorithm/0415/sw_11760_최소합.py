import sys
sys.stdin = open('sw_11760_최소합_input.txt', 'r')

dx = [0,1]
dy = [1,0]
def search(x, y, num):
    global min_ans
    if min_ans <= num:
        return 0
    if x == N-1 and y == N-1:
        ans.append(num)
        min_ans = num
        return 0
    visited[x][y] = 1
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and visited[nx][ny] == 0:
            search(nx, ny, num+arr[nx][ny])
    visited[x][y] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = []
    min_ans = 999999
    search(0,0,arr[0][0])
    print('#{} {}'.format(tc,min(ans)))