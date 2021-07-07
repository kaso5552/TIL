# 소수(prime number)란 1보다 큰 자연수 중 1과 자기 자신 두 개만을 약수로 갖는 수를 말한다.
#
# 합성수(composite number)란 1보다 큰 자연수 중 소수가 아닌 수를 말하며 3개 이상의 약수를 갖는다.
#
# 1은 소수도 합성수도 아니다.
#
# 5개의 자연수를 입력받아 소수인지 합성수인지를 판단하는 프로그램을 작성하시오.​

def checkPrime(n):
    # 시간초과방지를 위해서 제곱근을 사용하자
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "composite number"
    return "prime number"
num = list(map(int,input().split()))

for number in num:
    if number == 1:
        print("number one")
    else:
        print(checkPrime(number))
