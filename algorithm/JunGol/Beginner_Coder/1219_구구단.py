# 구구단을 출력하는 프로그램
# (1) 구간의 처음과 끝을 입력받는다.
# (2) 입력된 구간은 반드시 처음 입력 값이 끝의 입력 값보다 작아야 하는 것은 아니다.

T = 10
for tc in range(1, T+1):
    s, e = map(int,input().split())
    if 1 < s < 10 and 1 < e < 10:
        if s > e:

            for j in range(1, 10):
                for i in range(s, e-1, -1):
                    if i == e:
                        print(f'{i} * {j} = {i * j:>2}')
                    else:
                        print(f'{i} * {j} = {i * j:>2}', end='   ')
        else:

            for j in range(1, 10):
                for i in range(s, e+1):
                    if i == e:
                        print(f'{i} * {j} = {i * j:>2}')
                    else:
                        print(f'{i} * {j} = {i * j:>2}', end='   ')
    else :
        print('INPUT ERROR!')