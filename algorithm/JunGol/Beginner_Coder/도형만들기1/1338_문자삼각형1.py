# 삼각형의 높이 N을 입력받아서 아래와 같이 문자 'A'부터 차례대로 왼쪽 대각선으로 채워서 삼각형 모양을 출력하는 프로그램을 작성하시오.
# (1) 오른쪽 위부터 왼쪽 아래쪽으로 이동하면서 문자 'A'부터 차례대로 채워나간다.
# (2) N번 행까지 채워지면 다시 오른쪽 둘째 행부터 왼쪽 아래로 채워나간다.
# (3) 삼각형이 모두 채워질 때까지 반복하면서 채워 나간다. (문자 'Z'다음에는 'A'부터 다시 시작한다.)

N = int(input())
data = [[' ' for _ in range(N)] for _ in range(N)]
ch = 'A'
for i in range(N):
    for j in range(N):
        if i + j > N - 1:
            break
        data[i+j][N-1-j] = ch
        if ch == 'Z':
            ch = 'A'
        else:
            ch = chr(ord(ch) + 1)

for i in range(N):
    for j in range(N):
        print(data[i][j],end = ' ')
    print()
