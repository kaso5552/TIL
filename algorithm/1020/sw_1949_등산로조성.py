import sys
sys.stdin = open('sw_1949_등산로조성_input.txt', 'r')

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def solve():
    Q = height_list
    ans = 0
    while Q:
        sx, sy, h, temp_ans, is_build, visited = Q.pop(0)
        if ans < temp_ans:
            ans = temp_ans
        for d in range(4):
            nx = sx + dx[d]
            ny = sy + dy[d]
            is_visited = 0
            if 0 <= nx < N and 0 <= ny < N:
                for bx, by in visited:
                    if bx == nx and by == ny:
                        is_visited = 1
                        break
                if is_visited:
                    continue
                if arr[nx][ny] < h :
                    new_visited = visited[:]
                    new_visited.append([nx,ny])
                    Q.append([nx,ny,arr[nx][ny], temp_ans + 1, is_build, new_visited])
                elif arr[nx][ny] - h < K and is_build == 0:
                    new_visited = visited[:]
                    new_visited.append([nx,ny])
                    Q.append([nx,ny, h-1 , temp_ans + 1, 1, new_visited])

    return ans


T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    height = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] > height:
                height = arr[x][y]
                height_list = [[x,y,height,1,0,[[x,y]]]]
            elif arr[x][y] == height:
                height_list.append([x,y,height,1,0,[[x,y]]])

    print(f'#{tc} {solve()}')