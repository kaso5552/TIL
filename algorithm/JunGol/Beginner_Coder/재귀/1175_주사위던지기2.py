# 자연수 N과 M을 입력 받아서 주사위를 N번 던져서 나온 눈의 합이 M이 나올 수 있는 모든 경우를 출력하는 프로그램을 작성하시오.

def dice(n, k, s):
    if s > M or n > 6:
        return 0
    if k == N:
        if s == M:
            for i in range(N):
                for j in range(1, 7):
                    if visited[i][j] == 1:
                        print(j, end=' ')
            print()
        else:
            return 0
    else:
        visited[k][n] = 1
        dice(1, k+1, s+n)
        visited[k][n] = 0
        dice(n+1, k, s)


N, M = map(int,input().split())
visited = [[0] * 7 for _ in range(N)]
dice(1, 0, 0)