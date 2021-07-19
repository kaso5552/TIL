# 근우는 오늘 재미있는 카드 게임을 배우고 있다.
#
# 카드는 빨간색, 파란색, 노란색, 녹색의 네 가지 색이 있고, 색깔별로 1부터 9까지 숫자가 쓰여진 카드가 9장씩 있다.
#
# 카드는 모두 36(=4x9)장이다. 근우가 배운 카드 게임은 36장의 카드에서 5장을 뽑고, 아래와 같은 규칙으로 점수를 계산하는 것이다.
#
#
#
# 각 카드는 다음과 같이 나타낸다.
#
# 카드의 색깔은 영어 대문자 R, B, Y, G로 나타내는데, R은 빨간색, B는 파란색, Y는 노란색, G는 녹색을 뜻한다.
#
# 예를 들어서 Y8은 노란색 8을 나타내고, B5는 파란색 5를 나타낸다.
#
#
#
# <점수를 정하는 규칙>
#
# ① 카드 5장이 모두 같은 색이면서 숫자가 연속적일 때, 점수는 가장 높은 숫자에 900을 더한다.
#
#    예를 들어, 카드가 Y4, Y3, Y2, Y5, Y6 일 때 점수는 906(=6+900)점이다.
#
#
# ② 카드 5장 중 4장의 숫자가 같을 때 점수는 같은 숫자에 800을 더한다.
#
#    예를 들어, 카드가 B3, R3, B7, Y3, G3 일 때 점수는 803(=3+800)점이다.
#
#
# ③ 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다.
#
#    예를 들어, 카드가 R5, Y5, G7, B5, Y7 일 때 점수는 757(=5x10+7+700)점이다.
#
#
# ④ 5장의 카드 색깔이 모두 같을 때 점수는 가장 높은 숫자에 600을 더한다.
#
#    예를 들어, 카드가 Y3, Y4, Y8, Y6, Y7 일 때 점수는 608(=8+600)점이다.
#
#
# ⑤ 카드 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다.
#
#    예를 들어 R7, R8, G9, Y6, B5 일 때 점수는 509(=9+500)점이다.
#
#
# ⑥ 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
#
#    예를 들어 R7, Y7, R2, G7, R5 일 때 점수는 407(=7+400)점이다.
#
#
# ⑦ 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때
#
#   점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
#
#   예를 들어, R5, Y5, Y4, G9, B4 일 때 점수는 354(=5X10+4+300)점이다.
#
#
# ⑧ 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다.
#
#   예를 들어, R5, Y2, B5, B3, G4 일 때 점수는 205(=5+200)점이다.
#
#
# ⑨ 위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다.
#
#    예를 들어, R1, R2, B4, B8, Y5 일 때 점수는 108(=8+100)점이다.
#
#
#
#  입력으로 카드 5장이 주어질 때, 카드 게임의 점수를 구하는 프로그램을 작성하시오.
#
# 두 가지 이상의 규칙을 적용할 수 있는 경우에는 가장 높은 점수가 카드 게임의 점수이다.
#
def checkColor():
    max_num = 0
    for i in range(4):
        if sum(arr[i]) == 5:
            for j in range(1,6):
                if sum(arr[i][j:j+5]) == 5:
                    return 900 + j + 4
            for j in range(1,10):
                if arr[i][j] == 1:
                    max_num = j
            return 600 + max_num
    for i in range(1,10):
        if checknum[i] != 0:
            max_num = i
        if checknum[i] == 4:
            return 800 + i
        elif checknum[i] == 3:
            for j in range(i+1,10):
                if checknum[i] == 2:
                    return i * 10 + j + 700
            return 400 + i
        elif checknum[i] == 1 and i < 6:
            for j in range(i+1,i+5):
                if checknum[j] != 1:
                    break
                if j == i+4:
                    return 500 + i + 4
        elif checknum[i] == 2:
            for j in range(i+1,10):
                if checknum[j] == 2:
                    return j * 10 + i + 300
                elif checknum[j] == 3:
                    return j * 10 + i + 700
            return 200 + i
    return 100 + max_num

arr = [[0 for _ in range(10)] for _ in range(4)] # 1 ~ 9, 4개종류 카드(R,B,Y,G)
checknum = [0 for _ in range(10)]
for i in range(5):
    c, n = input().split()
    n = int(n)
    if c == 'R':
        arr[0][n] = 1
    elif c == 'B':
        arr[1][n] = 1
    elif c == 'Y':
        arr[2][n] = 1
    else:
        arr[3][n] = 1
    checknum[n] += 1
ans = checkColor()
print(ans)