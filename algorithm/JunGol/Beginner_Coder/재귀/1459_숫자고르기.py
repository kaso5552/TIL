# 세로 두 줄, 가로로 N개의 칸으로 이루어진 표가 있다.
#
# 첫째 줄의 각 칸에는 정수 1, 2, …, N이 차례대로 들어 있고 둘째 줄의 각 칸에는 1이상 N이하인 정수가 들어 있다.
#
# 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과,
#
# 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치한다.
#
# 이러한 조건을 만족시키도록 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램을 작성하시오.
#
#
#
# 예를 들어, N=7인 경우 아래와 같이 표가 주어졌다고 하자.
#
#
#
#
#
#
#
#
# 이 경우에는 첫째 줄에서 1, 3, 5를 뽑는 것이 답이다.
#
# 첫째 줄의 1, 3, 5밑에는 각각 3, 1, 5가 있으며 두 집합은 일치한다.
#
# 이 때 집합의 크기는 3이다. 만약 첫째 줄에서 1과 3을 뽑으면, 이들 바로 밑에는 정수 3과 1이 있으므로 두 집합이 일치한다.
#
# 그러나, 이 경우에 뽑힌 정수의 개수는 최대가 아니므로 답이 될수 없다.
def check(s, n):
    if visited[n] != 0:
        if n == s:
            return 1
        else:
            return 0
    else:
        visited[n] += 1
        temp = check(s, arr[n-1])
        if not temp :
            visited[n] -= 1
            return 0
        return 1

N = int(input())
arr = list(int(input()) for _ in range(N))
visited = [0] * (N + 1)
for i in range(N):
    check(i + 1, i + 1)
print(sum(visited))
for i in range(1, N+1):
    if visited[i] != 0:
        print(i)