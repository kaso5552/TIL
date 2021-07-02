# 삼각형의 높이 n과 종류 m을 입력받은 후 다음과 같은 삼각형 형태로 출력하는 프로그램을 작성하시오.

n, m = map(int,input().split())

if 1 <= n <= 100 and n % 2 == 1 and 1 <= m <= 3:
    arr = []
    if m == 1:
        cnt = 1
        for i in range(1, n+1):
            if i % 2 == 1:
                for j in range(cnt, cnt + i):
                    print(j,end=' ')
            else:
                for j in range(cnt + i - 1, cnt-1 , - 1):
                    print(j,end=' ')
            cnt += i
            print()

    elif m == 2:
        for i in range(0, n):
            print(' ' * i * 2,end='')
            for j in range(1, 2*(n-i)):
                print(i,end=' ')
            print()
    else:
        for i in range(1,n + 1):
            if i <= (n // 2 + 1):
                for j in range(1, i+1):
                    print(j,end=' ')
            else:
                for j in range(1, n - i + 2):
                    print(j,end=' ')
            print()
else:
    print('INPUT ERROR!')