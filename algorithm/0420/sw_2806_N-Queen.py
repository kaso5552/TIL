import sys
sys.stdin = open('sw_2806_N-Queen_input.txt', 'r')

dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
def powerset(n, k):
    global ans
    if n == k:
        ans += 1
    else:
        for i in range(n):
            if arr[k][i] != 0 : continue

            arr[k][i] = k+1
            for j in range(8):
                nx = k + dir[j][0]
                ny = i + dir[j][1]
                while 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = k+1
                    nx += dir[j][0]
                    ny += dir[j][1]

            powerset(n, k+1)
            arr[k][i] = 0
            for j in range(8):
                nx = k + dir[j][0]
                ny = i + dir[j][1]
                while 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == k+1:
                        arr[nx][ny] = 0
                    nx += dir[j][0]
                    ny += dir[j][1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]* N for _ in range(N)]
    ans = 0
    powerset(N,0)
    print('#{} {}'.format(tc, ans))


