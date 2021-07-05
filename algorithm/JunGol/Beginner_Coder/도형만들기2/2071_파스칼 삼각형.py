# 파스칼 삼각형이란 아래 <표1> 과 같은 자신의 왼쪽 위의 좌표와 오른쪽 위의 좌표 값을 더해서 값을 계속 갱신해 나가는 형태의 삼각형을 말한다.
#
# 아래와 같은 파스칼 삼각형의 높이 n과 종류 m을 입력 받은 후 다음과 같은 형태의 파스칼 삼각형을 출력하는 프로그램을 작성하시오.

n, m = map(int,input().split())

arr = [['' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i,n):
        if 0 < j and 0 < i and arr[j-1][i] and arr[j-1][i-1]:
            cnt = arr[j-1][i-1] + arr[j-1][i]
        else:
            cnt = 1
        arr[j][i] = cnt

if m == 1:
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
elif m == 2 :
    for i in range(n):
        print(' ' * i, end='')
        for j in range(n):
            print(arr[n-1-i][j],end=' ')
        print()
else:
    for i in range(n-1,-1,-1):
        for j in range(n-1, i-1 , -1):
            print(arr[j][i],end=' ')
        print()