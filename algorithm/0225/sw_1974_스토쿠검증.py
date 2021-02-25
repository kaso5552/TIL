import sys
sys.stdin = open('sw_1974_스토쿠검증_input.txt','r')

def Sudoku():

    # 행검사
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[i][j]] += 1
        for j in range(1, 10):
            if count[j] != 1:
                return 0
    # 열검사
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[j][i]] += 1
        for j in range(1, 10):
            if count[j] != 1:
                return 0
    # 박스검사
    for i in range(0,9,3):
        for j in range(0,9,3):
            count = [0] * 10
            for k in range(3):
                for s in range(3):
                    count[arr[k+i][s+j]] += 1
            for k in range(1, 10):
                if count[k] != 1:
                    return 0
    return 1

T = int(input())
for tc in range(1,T+1):
    arr = list(list(map(int,input().split())) for _ in range(9))
    ans = Sudoku()
    print('#{} {}'.format(tc,ans))