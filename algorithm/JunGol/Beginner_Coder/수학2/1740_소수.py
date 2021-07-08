# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.
#
#
#
# 예를 들어 M=60, N=100이 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
#
# 이들 소수의 합은 620이고, 최소값은 61이 된다.
def isPrime(n):

    if n < 2:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0

    return n


M = int(input())
N = int(input())

min_num = 99999
sum_num = 0
for i in range(M, N+1):
    if isPrime(i):
        if min_num > i :
            min_num = i
        sum_num += i

if sum_num == 0:
    print(-1)
else:
    print(f'{sum_num}\n{min_num}')