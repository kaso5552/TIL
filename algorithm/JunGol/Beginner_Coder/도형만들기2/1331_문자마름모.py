# 마름모의 한 변의 길이 N을 입력 받아 아래와 같이 문자 마름모를 출력하는 프로그램을 작성하시오.
#
#
#
# < 처리조건 >
#
# (1) 첫 번째 행의 중앙부터 출발하여 시계 반대 방향으로 'A' 부터 차례대로 채워나간다. ('Z'다음에는 다시 'A'가 된다.)
#
# (2) 바깥 부분이 다 채워지면 두 번째 행 중앙부터 다시 같은 작업을 반복한다.
#
# (3) 같은 방법으로 마름모를 다 채워지도록 하여 출력한다.

def get_alpha(temp):
    if temp == 'Z':
        temp = 'A'
    else:
        temp = chr(ord(temp) + 1)

    return temp

N = int(input())
arr = [[' ' for _ in range(2 * N - 1)] for _ in range(2 * N -1)]

alpha = 'B'
cnt = N - 1
x, y = 0, N-1

arr[0][N-1] = 'A'
while cnt > 0:
    for i in range(cnt):
        x += 1
        y -= 1
        arr[x][y] = alpha
        alpha = get_alpha(alpha)

    for i in range(cnt):
        x += 1
        y += 1
        arr[x][y] = alpha
        alpha = get_alpha(alpha)


    for i in range(cnt):
        x -= 1
        y += 1
        arr[x][y] = alpha
        alpha = get_alpha(alpha)

    cnt -= 1

    for i in range(cnt):
        x -= 1
        y -= 1
        arr[x][y] = alpha
        alpha = get_alpha(alpha)

    y -= 1
    arr[x][y] = alpha
    alpha = get_alpha(alpha)

for i in range(2 * N -1):
    for j in range(2 * N -1):
        print(arr[i][j],end=' ')
    print()
