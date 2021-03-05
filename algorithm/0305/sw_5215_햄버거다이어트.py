import sys

sys.stdin = open('sw_5215_햄버거다이어트_input.txt', 'r')


def Powerset(n, k, s, c):  # s : 맛의 점수의 합 , c : 칼로리의 합
    global ans
    if c > L:
        return
    elif n == k:
        if ans < s:
            ans = s
    else:
        visited[k] = 1
        Powerset(n, k + 1, s + arr[k][0], c + arr[k][1])
        visited[k] = 0
        Powerset(n, k + 1, s, c)


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    number = []
    ans = 0
    Powerset(N, 0, 0, 0)
    print('#{} {}'.format(tc, ans))
