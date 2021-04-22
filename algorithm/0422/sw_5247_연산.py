import sys
sys.stdin = open('sw_5247_연산_input.txt', 'r')

from collections import deque

def cal(n, k):
    if k == 0:
        return n+1
    elif k == 1:
        return n-1
    elif k == 2:
        return n * 2
    else:
        return n - 10
def fun(n):
    global ans

    Q.append((n,0))

    while len(Q) != 0:
        num, count = Q.popleft()
        if num == M:
            ans = count
            return
        for i in range(4):
            num2 = cal(num, i)
            if 1000000 >= num2 > 0 and visited[num2] == 0:
                Q.append((num2,count+1))
                visited[num2] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    ans = 999999999
    Q = deque()
    visited = [0] * 1000001
    fun(N)

    print('#{} {}'.format(tc, ans))