import sys
sys.stdin = open('sw_1247_최적경로_input.txt', 'r')

def fun():
    for i in range(N+2):
        for j in range(N+2):
            data[i][j] = abs(arr[2*i] - arr[2*j]) + abs(arr[2*i +1] - arr[2*j +1])

def perm(n, k, s, t):
    global ans
    if t > ans:
        return 0
    if n == k:
        t += data[s][1]
        if ans > t:
            ans = t
        return 0
    else:
        for i in range(2,N+2):
            if visited[i] == 1: continue
            visited[i] = 1
            perm(n, k+1, i, t+data[s][i])
            visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    data = [[0] * (N+2) for _ in range(N+2)] # 0 : 회사  1 ~ N : 고객집 N+1: 집
    visited = [0] * (N+2)
    fun()
    ans = 999999
    perm(N,0,0,0)
    print('#{} {}'.format(tc,ans))