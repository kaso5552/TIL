# 삼각형의 높이 n과 종류 m을 입력 받은 후 다음과 같은 삼각형 형태로 출력하는 프로그램을 작성하시오.

n, m = map(int,input().split())

if 1 <= n <= 100 and 1 <= m <= 3:
    if m == 1:
        for i in range(1, n+1):
            print('*' * i)
    elif m == 2:
        for i in range(n,0,-1):
            print('*' * i)
    else:
        for i in range(n-1,-1,-1):
            print(' ' * i , end='')
            print('*' * (2*n-1-2 * i))
else:
    print("INPUT ERROR!")