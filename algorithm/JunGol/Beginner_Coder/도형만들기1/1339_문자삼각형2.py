# 삼각형의 높이 N을 입력받아서 아래와 같이 문자 'A'부터 차례대로 맨 오른쪽 가운데 행부터 차례대로 아래와 같이 채워서
# 삼각형 모양을 출력하는 프로그램을 작성하시오.
# (1) 오른쪽 가운데 행에 문자 'A'를 채우고 왼쪽 열로 이동하여 위에서 아래로 채워나간다.
# (2) 가장 왼쪽 행까지 반복하여 모두 채워 나간다. (문자 'Z'다음에는 'A'부터 다시 시작한다.)

N = int(input())
if 1 <= N <= 100 and N % 2 == 1:
    data = [[' ' for _ in range(N)] for _ in range(N)]
    ch = 'A'
    middle = int(N / 2)
    count = -1
    for i in range(middle, -1, -1):
        count += 1
        for j in range(middle - count, middle + count + 1):
            data[j][i] = ch
            if ch == 'Z':
                ch = 'A'
            else:
                ch = chr(ord(ch) + 1)
    for i in range(N):
        for j in range(N):
            print(data[i][j], end=' ')
        print()
else:
    print('INPUT ERROR')