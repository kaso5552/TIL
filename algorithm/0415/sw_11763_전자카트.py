import sys
sys.stdin = open('sw_11763_전자카트_input.txt', 'r')

def fun(n, k):
    if n == k:
        stack.append(office_sample[:])
    else:
        for i in range(n):
            if office_visited[i]: continue

            office_sample[k] = office[i]
            office_visited[i] = 1
            fun(n, k+1)
            office_visited[i] = 0

def office_sum():
    global ans
    for i in range(len(stack)):
        result = arr[0][stack[i][0]-1]
        for j in range(N-2):
            result += arr[stack[i][j]-1][stack[i][j+1]-1]
        result += arr[stack[i][-1]-1][0]
        if ans > result:
            ans = result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    office = []
    office_visited = [0] * (N-1)
    office_sample = [0] * (N-1)
    stack = []
    ans = 9999999
    for i in range(2,N+1):
        office.append(i)
    fun(N-1, 0)
    office_sum()
    print('#{} {}'.format(tc,ans))


