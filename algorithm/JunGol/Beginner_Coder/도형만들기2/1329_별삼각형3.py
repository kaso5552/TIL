# 삼각형의 높이 N을 입력받아 아래와 같은 모양을 출력하는 프로그램을 작성하시오.

N = int(input())

if 1 <= N <= 100 and N % 2 == 1:
    for i in range(N//2+1):
        print(' '*i,end='')
        print('*' * (1 + 2 * i))
    for i in range(N//2-1,-1,-1):
        print(' '*i,end='')
        print('*' * (1 + 2 * i))
else:
    print('INPUT ERROR!')