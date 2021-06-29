# 주어진 정수들 중 입력 받은 수의 약수와 배수의 합을 각각 출력하라.
# 예를 들면,
# 6개의 정수 2, 3, 5, 12, 18, 24 가 주어지고 12를 입력 받은 경우
# 12의 약수는 2, 3, 12 이고
# 12의 배수는 12, 24 이다.

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
ans1 = 0
ans2 = 0
for i in range(n):
    if arr[i] < m :
        if m % arr[i] == 0:
            ans1 += arr[i]
    elif arr[i] == m:
        ans1 += m
        ans2 += m
    else:
        if arr[i] % m == 0:
            ans2 += arr[i]

print(ans1)
print(ans2)