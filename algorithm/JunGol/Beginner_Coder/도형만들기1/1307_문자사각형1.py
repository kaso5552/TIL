# 정사각형의 한 변의 길이 n을 입력받은 후 다음과 같은 문자로 된 정사각형 형태로 출력하는 프로그램을 작성하시오.
# 문자의 진행 순서는 맨 오른쪽 아래에서 위쪽으로 'A'부터 차례대로 채워나가는 방법으로 아래 표와 같이 왼쪽 위까지 채워 넣는다.
# 'Z' 다음에는 다시 'A'부터 반복된다.

n = int(input())
data = [ ['' for _ in range(n)] for _ in range(n)]
ch = 'A'
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        data[j][i] = ch
        if ch == 'Z':
            ch = 'A'
        else:
            ch = chr(ord(ch) + 1)

for i in range(n):
    for j in range(n):
        print(data[i][j],end=' ')
    print()