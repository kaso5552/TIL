# 1부터 어떤 양의 정수 n까지의 정수를 모두 곱한 것을 말하며 n!로 나타낸다.
#
#
# 0! = 1
#
# 1! = 1
#
# 2! = 2
#
# n! = n * (n-1)!
#
# ：
#
# 와 같이 정의된다.
#
#
#
# 예로 4! = 4×3×2×1 = 24 이다.
#
#
#
# n! 이 주어졌을 때 결과를 출력하는 프로그램을 작성하라.
#
#
#
# * 결과가 int범위를 넘는 경우
#
# 자료형 long long
#
# 입력/출력 서식문자 %lld
#
# 를 사용한다.
def fac(n):
    global ans
    if n == 0 :
        return 0
    elif n == 1:
        print('1! = 1')
    else:
        ans *= n
        print(f'{n}! = {n} * {n-1}!')
    fac(n-1)

N = int(input())
ans = 1
fac(N)
print(ans)
