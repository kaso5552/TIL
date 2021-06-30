# n개의 정수를 입력받아서 최대공약수와 최소공배수를 구하는 프로그램을 작성하여 보자.


def get_gcd(A, B):
    ret = 0
    for i in range(1, A+1):
        if A % i == 0 and B % i == 0:
           ret = i

    return ret

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
gcd = arr[0]
lcm = arr[0]

for i in range(1, N):
    gcd = get_gcd(gcd, arr[i])
    lcm = int(lcm / get_gcd(lcm, arr[i])) * arr[i]

print(gcd, lcm)