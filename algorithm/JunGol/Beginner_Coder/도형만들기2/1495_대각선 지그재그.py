# 정사각형의 크기를 입력 받은 후 대각선으로 지그재그 형태인 다음과 같은 형태로 출력하는 프로그램을 작성하시오.
#
#
#
# < 처리조건>
#
# (1) 가장 왼쪽 위의 좌표부터 차례로 숫자를 대입시킨다.
#
# (2) 대각선을 기준으로 계속 지그재그 모양으로 채워져야 하며 숫자는 1씩 증가하는 형태로 채워나가야 한다.

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

x, y = 0, 0
arr[x][y] = 1
cnt = 2
while cnt < n * n :
    # 아래로 한칸 ( 불가능하면 오른쪽 )
    if x < n - 1:
        x += 1
    else:
        y += 1

    arr[x][y] = cnt
    cnt += 1


    # 오른쪽 위로 최대
    while 0 < x and y < n - 1 :
        x -= 1
        y += 1
        arr[x][y] = cnt
        cnt += 1

    # 오른쪽으로 한칸 ( 불가능하면 아래 )
    if y < n - 1 :
        y += 1
    else:
        x += 1

    arr[x][y] = cnt
    cnt += 1

    # 왼쪽아래로 최대
    while x < n - 1 and 0 < y :
        x += 1
        y -= 1
        arr[x][y] = cnt
        cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()