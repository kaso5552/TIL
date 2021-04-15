import sys
sys.stdin = open('sw_4012_요리사_input.txt', 'r')

def fun(n, k):
    global ans
    if n == N//2:
        A = []
        B = []
        for i in range(N):
            if visited[i] == 1:
                A.append(i)
            else:
                B.append(i)
        ta = 0
        tb = 0
        for i in range(len(A)-1):
            for j in range(i,len(A)):
                ta += arr[A[i]][A[j]]
                tb += arr[B[i]][B[j]]
        if ans > abs(ta-tb):
            ans = abs(ta-tb)

    else:
        for i in range(k, N):
            if visited[i] == 1 : continue
            visited[i] = 1
            fun(n+1, i+1)
            visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total = 0
    for i in range(N-1):
        for j in range(i, N):
            temp = arr[i][j] + arr[j][i]
            total += temp
            arr[i][j] = arr[j][i] = temp
    visited= [0] * N
    ans = 999999
    fun(0, 0)
    print('#{} {}'.format(tc, ans))


