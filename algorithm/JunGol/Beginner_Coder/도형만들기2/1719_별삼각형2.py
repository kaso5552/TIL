# 삼각형의 높이 n과 종류 m을 입력 받은 후 다음과 같은 삼각형 형태로 출력하는 프로그램을 작성하시오.
# 다음은 n이 5인 경우의 예시이다.

n, m = map(int,input().split())

if 1 <= n <= 100 and n % 2 != 0 and 1 <= m <= 4:
    if m == 1:
        for i in range(1, n//2 + 2):
            print('*' * i)
        for i in range(n//2, 0, -1):
            print('*' * i)
    elif m == 2:
        for i in range(n//2, -1,-1):
            print(' ' * i, end='')
            print('*' * (n//2 + 1 - i))
        for i in range(1, n//2 + 1):
            print(' ' * i, end='')
            print('*' * (n//2 + 1 - i))
    elif m == 3:
        for i in range(n//2+1):
            print(' '* i, end='')
            print('*' * (n - 2 * i))
        for i in range(n//2-1,-1,-1):
            print(' '* i, end='')
            print('*' * (n - 2 * i))
    else:
        for i in range(n//2+1):
            print(' '* i, end='')
            print('*' * (n//2 + 1 - i))
        for i in range(2, n//2 + 2):
            print(' '* (n//2),end='')
            print('*' * i)
else:
    print("INPUT ERROR!")