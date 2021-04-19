import sys
sys.stdin = open('sw_1861_정사각형방_input.txt', 'r')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def fun():
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[i][j] + 1 == arr[nx][ny]:
                        data[arr[i][j]] = 1

def result():
    global ans_num, ans_count
    result_number = 0
    result_count = 0
    for i in range(N ** 2):
        if data[i] == 0 and data[i+1] == 1:
            result_number = i + 1
            result_count += 1
        elif data[i] == 1 and data[i+1] == 1:
            result_count += 1
        elif data[i] == 1 and data[i+1] == 0:
            result_count += 1
            if result_count > ans_count:
                ans_num = result_number
                ans_count = result_count
            result_count = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    data = [0] + [0] * (N ** 2)
    fun()
    ans_num, ans_count = 99999999, 0
    result()
    print('#{} {} {}'.format(tc,ans_num,ans_count))