import sys
sys.stdin = open('sw_2819_숫자붙이기_input.txt', 'r')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def fun(x,y,k):
    global ans
    if len(k) == 7:
        ans.add(k)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 3 and 0 <= ny <= 3:
                fun(nx,ny, k + arr[nx][ny])

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            fun(i,j, arr[i][j])
    print('#{} {}'.format(tc,len(ans)))

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# def fun(x,y,k):
#     global ans
#     if len(k) == 7:
#         if not (k in ans):
#             ans.append(k)
#         return
#     else:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx <= 3 and 0 <= ny <= 3:
#                 fun(nx,ny, k + arr[nx][ny])
#
# T = int(input())
# for tc in range(1,T+1):
#     arr = [list(input().split()) for _ in range(4)]
#     ans = []
#     for i in range(4):
#         for j in range(4):
#             fun(i,j, arr[i][j])
#     print('#{} {}'.format(tc,len(ans)))
