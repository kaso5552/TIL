# 사각형의 높이 n과 너비 m을 입력받은 후
# n행 m열의 사각형 형태로 1부터 n*m번까지 숫자가 차례대로 출력되는 프로그램을 작성하시오.

n, m = map(int,input().split())

for i in range(n):
    for j in range(i * m + 1, i * m + m + 1 ):
        print(j, end=' ')
    print()
