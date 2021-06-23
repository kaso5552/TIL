# 원하는 구구단의 범위를 입력받아 해당 구간의 구구단을 출력하는 프로그램을 작성하시오.
# 시작 범위와 끝 범위사이의 구구단을 출력하되
# 모든 값과 부호 사이는 공백으로 구분하여 줄을 맞추어 출력해야 한다.
# 식과 식 사이는 3개의 공백으로 구분하고 구구단 사이에는 한 줄을 비워 두도록 한다.

T = 10
for tc in range(1, T+1):
    s, e = map(int,input().split())
    if 1 < s < 10 and 1 < e < 10:
        if s > e:
            for i in range(s, e-1, -1):
                for k in range(1, 10, 3):
                    for j in range(k, k+3):
                        print(f'{i} * {j} = {i*j:>2}', end='   ')
                    print()
                print()
        else:
            for i in range(s, e+1):
                for k in range(1, 10, 3):
                    for j in range(k, k+3):
                        print(f'{i} * {j} = {i*j:>2}', end='   ')
                    print()
                print()
