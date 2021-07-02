# 삼각형의 높이 N을 입력받아서 아래와 같이 숫자 0부터 달팽이 모양으로 차례대로 채워진 삼각형을 출력하는 프로그램을 작성하시오.
#
# < 처리조건 >
# 왼쪽 위부터 시계방향으로 오른쪽 아래로 이동하면서 숫자 0부터 N개를 채우고
# 다시 왼쪽으로, 다음은 위쪽으로 반복하면서 채워 나간다. (숫자 9 다음에는 0부터 다시 시작한다.)

N = int(input())
dir = [(1, 1), (0, -1), (-1, 0)]
ans = [['' for _ in range(N)] for _ in range(N)]
sum = 0
for i in range(1, N+1):
    sum += i
cnt, t_cnt = 0, 0 # cnt는 배열에 들어가는 숫자(0~9) t_cnt는 들어가는 숫자의 갯수
dir_cnt = 0
x,y = -1, -1

while t_cnt < sum:
    x = x + dir[dir_cnt][0]
    y = y + dir[dir_cnt][1]
    if 0 <= x < N and 0 <= y < N :
        if ans[x][y] != '':
            x = x - dir[dir_cnt][0]
            y = y - dir[dir_cnt][1]
            dir_cnt += 1
            dir_cnt %= 3
        else:
            ans[x][y] = cnt
            if cnt == 9:
                cnt = 0
            else:
                cnt += 1
            t_cnt += 1
    else:
        x = x - dir[dir_cnt][0]
        y = y - dir[dir_cnt][1]
        dir_cnt += 1
        dir_cnt %= 3

for i in range(N):
    for j in range(N):
        print(ans[i][j],end=' ')
    print()