# 정사각형의 한 변의 길이 n과 종류 m을 입력받은 후 다음과 같은 정사각형 형태로 출력하는 프로그램을 작성하시오.

n, m = map(int,input().split())

for i in range(1, n + 1):
    if m == 1:
        for j in range(n):
            print(i, end=' ')
    elif m == 2:
        if i % 2 == 1:
            for j in range(1, n+1, 1):
                print(j,end=' ')
        else:
            for j in range(n, 0, -1):
                print(j, end=' ')
    else:
        for j in range(i, i*n+1, i):
            print(j, end=' ')
    print()