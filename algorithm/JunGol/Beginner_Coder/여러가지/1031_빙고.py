# 빙고 게임은 다음과 같은 방식으로 이루어진다.
#
# 먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다.
#
#
#
#
#
# 다음은 사회자가 부르는 수를 차례로 지워나간다.
#
# 예를 들어 5 10 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.
#
#
#
#
#
#
# 차례로 수를 지워가다가 같은 가로줄 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.
#
#
#
#
#
# 이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데 가장 먼저 외치는 사람이 게임의 승자가 된다.
#
#
#
#
#
# 철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때
#
# 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.
def bingo():
    temp = 0
    for i in range(5):
        ans = 0
        if sum(arr[i]) == 0:
            temp += 1
        for j in range(5):
            if arr[j][i] != 0:
                ans = 1
                break
        if ans == 0:
            temp += 1
        ans = 0
        if i == 0 :
            for j in range(5):
                if arr[i+j][i+j] != 0:
                    ans = 1
                    break
            if ans == 0:
                temp += 1
        elif i == 4 :
            for j in range(5):
                if arr[i-j][j] != 0:
                    ans = 1
                    break
            if ans == 0:
                temp += 1
    return temp
def fill(n):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                arr[i][j] = 0
                if bingo() >= 3:
                    return 'bingo'
    return 0

def result():
    for i in range(5):
        for j in range(5):
            if fill(call[i][j]):
                print(i * 5 + j + 1)
                return 0

arr = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]
result()




