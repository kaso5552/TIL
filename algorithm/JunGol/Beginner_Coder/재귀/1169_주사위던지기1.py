# 주사위를 던진 횟수 N과 출력형식 M을 입력 받아서 M의 값에 따라 각각 아래와 같이 출력하는 프로그램을 작성하시오.
#
#
#
# M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우
#
# M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
#
# M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
#
#
#
# * 중복의 예
#
# 1 1 2 와 중복 : 1 2 1, 2 1 1
#
# 1 2 3 과 중복 : 1 3 2, 2 1 3, 2 3 1, 3 1 2​

def dice(n, k):
    if k == N:
        for i in range(N):
            for j in range(1, 7):
                if visited[i][j] == 1:
                    print(j, end=' ')
        print()
        return 0
    elif n > 6 :
        return 0
    else:
        visited[k][n] = 1
        if M == 1:
            dice(1, k+1)
        elif M == 2:
            dice(n, k + 1)
        elif M == 3:
            if k > 0 and check(k,n):
                pass

            else:
                dice(1, k+1)
        visited[k][n] = 0
        dice(n+1,k)

def check(k, n):
    for i in range(k-1, -1, -1):
        if visited[i][n] == 1:
            return 1
    return 0

N, M = map(int,input().split())
visited = [[0] * 7 for _ in range(N)]
dice(1, 0)