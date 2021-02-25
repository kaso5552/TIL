import sys
sys.stdin = open('sw_2805_농작물 수확하기_input.txt','r')

def Count():
    result = 0
    n = N//2
    for i in range(N):
        result += arr[n][i]
    for i in range(1,n+1):
        for j in range(i,N-i):
            result += arr[n-i][j]
            result += arr[n+i][j]
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(list(map(int,input())) for _ in range(N))
    ans = Count()
    print('#{} {}'.format(tc,ans))