# 소수(prime number)란 1보다 큰 자연수 중 1과 자기 자신 두 개만을 약수로 갖는 수를 말한다.
#
# 자연수 M과 N을 입력받아 M부터 N까지 소수의 개수를 구하여 출력하는 프로그램을 작성하시오.

M, N = map(int,input().split())
arr = [1] * 2000001
arr[0], arr[1] = 0, 0
ans = 0

#에라토스테네스의 체
# 자연수를 체로 쳐서 걸러내고 소수만 골라내는 방법입니다.
for i in range(2, int(N ** 0.5) + 1):
    if arr[i] :
        for j in range(i*i, N+1, i):
            arr[j] = 0

for i in range(M,N+1):
    if arr[i]:
        ans += 1

print(ans)