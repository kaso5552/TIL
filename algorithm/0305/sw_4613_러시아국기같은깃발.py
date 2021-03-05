import sys
sys.stdin = open('sw_4613_러시아국기같은깃발_input.txt', 'r')


color_data = ['W', 'B', 'R']

# 색깔마다 차지하는 줄의 갯수를 리스트를만든다
def Color():
    sample = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            for k in range(1, N - 1):
                if i + j + k == N :
                    sample.append((i, j, k))
    return sample

def Funtion(data, col):
    start = 0
    count = 0
    for i in range(3):
        for j in range(start,start + col[i]):
            for k in range(M):
                if data[j][k] != color_data[i]:
                    count += 1
        start += col[i]
    return count


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(list(input()) for _ in range(N))
    color = Color() # 순서대로 흰, 파, 빨
    ans = 987654321
    for i in range(len(color)):
        result = Funtion(arr,color[i])
        if result < ans :
            ans = result
    print('#{} {}'.format(tc,ans))
