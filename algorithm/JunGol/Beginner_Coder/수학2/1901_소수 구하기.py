# 소수(prime number)란 2이상의 수로써 1과 자기 자신 외에는 약수를 갖지 않는 수를 의미한다.
#
# 임의의 M값에 대하여 M에 가장 가까운 소수를 구하는 프로그램을 아래 조건에 따라 작성한다.

# 첫 번째 줄에는 처리해야 할 수의 개수 N을 입력 받는다. (N은 100이하의 정수)
#
# 다음 줄에는 처리해야할 수 N개(M1부터 Mn까지)를 한 줄에 한 개씩 차례로 입력 받는다.
#
# (Mi 는 1,000,000 이하의 양의 정수)
#
# 데이터의 크기가 주어진 범위를 벗어나는 입력은 없다.

# 임의의 값 Mi에 대해 차이가 가장 작은 소수를 구하여 출력한다.
#
# 만약 차이가 같은 소수가 여러 개이면 작은 수부터 모두 출력한다.
#
# 출력되는 값은 1이상 1,000,000이하의 소수이어야 한다.
def isPrime(n):

    if n < 2 :
        return ''

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return ''

    return n

N = int(input())

for i in range(N):
    num = int(input())
    ans = 0
    ans2 = ''

    for j in range(num, 1, -1):
        if isPrime(j):
            ans = j
            break

    for j in range(num + 1, num + (num - ans)):
        if isPrime(j):
            ans = j
            break
    if num != ans:
        ans2 = isPrime(num + (num-ans))

    print(ans, ans2)

