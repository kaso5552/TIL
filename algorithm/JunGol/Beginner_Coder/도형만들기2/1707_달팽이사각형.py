# 정사각형의 크기를 입력 받은 후 시계 방향으로 돌면서 다음과 같은 형태로 출력하는 프로그램을 작성하시오.
#
#
#
# < 처리조건 >
#
# (1) 가장 왼쪽 위의 좌표부터 차례로 숫자를 대입 시킨다.
#
# (2) 오른쪽으로 채워 나가다가 끝이면 다시 아래 → 왼쪽 → 위 →오른쪽의 순으로 모두 채워질 때까지 반복한다.

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
num = 1
cnt = n
x, y = 0, -1

while cnt > 0 :
    for i in range(cnt):
        y += 1
        arr[x][y] = num
        num += 1

    cnt -= 1

    for i in range(cnt):
        x += 1
        arr[x][y] = num
        num += 1

    for i in range(cnt):
        y -= 1
        arr[x][y] = num
        num += 1

    cnt -= 1

    for i in range(cnt):
        x -= 1
        arr[x][y] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()