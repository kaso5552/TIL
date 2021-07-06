# ​홀수 정사각형의 크기를 입력 받은 후, 가로 세로 대각선의 합이 일정한 마방진을 출력하는 프로그램을 작성하시오.
#
# 마방진이란 1부터 N*N까지의 숫자를 한 번씩만 써서 정사각형에 배치하여 가로와 세로, 그리고 대각선의 합이 같도록 하는 것이다.
#
# 다음의 순서에 따라 각 위치에 차례대로 값을 넣는다.
# 1. 첫 번째 숫자인 1을 넣는 위치는 첫 번째 행 가운데이다.
# 2. 숫자가 N의 배수이면 바로 아래의 행으로 이동하여 다음의 수를 넣고
# 3. 그렇지 않으면 왼쪽 위로 이동하여 다음의 숫자를 넣는다.
#    만약 행이 첫 번째를 벗어나면 마지막 행으로 이동하고, 열이 첫 번째를 벗어나면 마지막 열로 이동한다.

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

x, y = 0, n // 2
cnt = 1
arr[x][y] = cnt


while cnt < n * n:
    if cnt % n == 0:
        x += 1
        cnt += 1
        arr[x][y] = cnt

    else:
        x -= 1
        y -= 1
        cnt += 1
        if x < 0 :
            x = n - 1
            arr[x][y] = cnt
        elif y < 0 :
            y = n - 1
            arr[x][y] = cnt
        else:
            arr[x][y] = cnt

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()