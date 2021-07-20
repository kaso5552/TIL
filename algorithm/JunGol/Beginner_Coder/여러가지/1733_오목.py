# 오목은 바둑판에 검은 바둑알과 흰 바둑알을 교대로 놓아서 겨루는 게임이다.
#
# 바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데
#
# 가로줄은 위에서부터 아래로 1번, 2번, ... ,19번의 번호가 붙고
#
# 세로줄은 왼쪽에서부터 오른쪽으로 1번, 2번, ... 19번의 번호가 붙는다.
#
#
#
#
#
#
#
# 위의 그림에서와 같이 같은 색의 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이기게 된다.
#
# 여기서 연속적이란 가로, 세로 또는 대각선 방향 모두를 뜻한다.
#
# 즉, 위의 그림은 검은색이 이긴 경우이다.
#
# 하지만 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.
#
#
#
# 입력으로 바둑판의 어떤 상태가 주어졌을 때, 검은색이 이겼는지,
#
# 흰색이 이겼는지 또는 아직 승부가 결정되지 않았는지를 판단하는 프로그램을 작성하시오.
#
# 단, 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.
dx = [-1,0,1,1]
dy = [1,1,1,0]
def check(n,x,y):
    for i in range(4):
        nx = x
        ny = y
        cnt = 0
        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19:
            if arr[x - dx[i]][y - dy[i]] == n:
                continue
        for j in range(6):
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == n:
                cnt += 1
                continue
            else:
                break
        if cnt == 4:
            return n
    return 0

def ans():
    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                ans = check(arr[i][j], i, j)
                if ans != 0:
                    print(f'{ans}\n{i+1} {j+1}')
                    return 0
    print(0)
arr = [list(map(int,input().split())) for _ in range(19)]
ans()