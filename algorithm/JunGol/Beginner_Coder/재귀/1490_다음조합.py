# 1부터 N까지의 N개의 정수 중에서 K개를 뽑아낼 때 가능한 경우들을 조합이라고 한다.
#
#
#
# 예를 들어 N=5고 K=3일 경우 가능한 모든 조합은 다음과 같다
#
#
#
# 1 2 3
#
# 1 2 4
#
# 1 2 5
#
# 1 3 4
#
# 1 3 5
#
# 1 4 5
#
# 2 3 4
#
# 2 3 5
#
# 2 4 5
#
# 3 4 5
#
#
#
# [ 1 2 3 ] 과 [ 3 1 2 ] 와 같이 순서는 다르나 뽑힌수가 같은 경우는 한가지로 간주한다.
#
# 다시 말해서 뽑힌 순서는 고려하지 않는다는 것이다.
#
#
#
# N과 K가 입력되고 N과 K에서 가능한 조합 중 하나가 입력될 경우,
#
#
#
# 조합들을 오름차순으로 정렬 했을 때 다음으로 나오는 조합을 출력하는 프로그램을 작성하라.
#
#
def powerSet(n, k):
    global ans
    if k == K:
        if ans == 1:
            for i in range(1,N+1):
                if visited[i] == 1:
                    print(i, end=' ')
            ans = 2
            return 0
        else:
            cnt = 0
            for i in range(1,N+1):
                if visited[i] == 1:
                    if temp[cnt] == i:
                        cnt += 1
                    else:
                        return 0
        ans = 1
    elif(n == N+1 or k > K):
        return 0
    else:
        visited[n] = 1
        a = powerSet(n+1,k+1)
        if a:
            return 0
        visited[n] = 0
        a = powerSet(n+1,k)
        if a:
            return 0

N, K = map(int,input().split())
temp = list(map(int,input().split()))
visited = [0] * (N + 1)
ans = 0
arr = list(i for i in range(0,N+1))
powerSet(1,0)
if ans != 2:
    print('NONE')
