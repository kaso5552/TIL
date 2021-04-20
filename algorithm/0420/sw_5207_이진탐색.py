import sys
sys.stdin = open('sw_5207_이진탐색_input.txt', 'r')

def search(n, l, r):
    global ans, c
    m = (l+r)//2
    if n == A[m]:
        ans += 1
        return 0
    elif n < A[m]:
        if c == 'left':
            return 0
        c = 'left'
        search(n, l, m-1)
    elif n > A[m]:
        if c == 'right':
            return 0
        c = 'right'
        search(n, m+1, r)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    ans = 0
    for i in B:
        if i in A:
            c = ''
            search(i, 0, len(A)-1)
    print('#{} {}'.format(tc,ans))