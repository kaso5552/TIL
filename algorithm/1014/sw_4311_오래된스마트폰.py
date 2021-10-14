import sys
sys.stdin = open('sw_4311_오래된스마트폰_input.txt', "r")

def solve():
    if visited[target] != 0:
        return visited[target]

    number = list(total_num)
    Q = [[_, visited[_]] for _ in number]

    while Q:
        num, check = Q.pop(0)
        for i in number:
            temp_num = i
            temp_check = visited[temp_num]
            for j in cal:
                ans_num = calcul(j, num, temp_num)

                if ans_num < 0 or ans_num > 999:
                    continue
                else:
                    ans_check = temp_check + check + 1

                    if ans_check >= M:
                        continue
                    else:
                        if visited[ans_num] == 0 or ans_check < visited[ans_num]:
                            visited[ans_num] = ans_check
                            Q.append((ans_num, ans_check))

    if visited[target] != 0:
        return visited[target] + 1

    return -1


def calcul(n, a, b):
    if n == 1:
        return a + b
    elif n == 2:
        return a - b
    elif n == 3:
        return a * b
    elif n == 4:
        if b != 0:
            return int(a/b)
        return -1


T = int(input())
for tc in range(1, T+1):
    N, O, M = map(int,input().split())
    num_list = list(map(int,input().split()))
    cal = list(map(int,input().split()))
    target = int(input())
    total_num = set()
    need_visit = []
    visited = [0] * 1000

    for num in num_list:
        need_visit.append([num, 1])
        visited[num] = 1

    while need_visit:
        number, check = need_visit.pop()
        total_num.add(number)

        if check < 3:
            for num in num_list:
                if number != 0:
                    new_number = number * 10 + num
                    need_visit.append([new_number, check + 1])
                    visited[new_number] = check + 1

    ans = solve()
    print(f'#{tc} {ans}')

