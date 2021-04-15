import sys
sys.stdin = open('sw_11765_화물토크_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    hour = [list(map(int,input().split())) for _ in range(N)]
    using = [0] * 25
    ans = 0
    for i in range(N-1):
        change = 0
        sample = hour[i][1]
        for j in range(i+1,N):
            if sample > hour[j][1]:
                sample = hour[j][1]
                change = j
        if change != 0:
            hour[i], hour[change] = hour[change], hour[i]
    end_hour = 0
    while hour:
        start, end = hour.pop(0)
        if start >= end_hour:
            ans += 1
            end_hour = end

    print('#{} {}'.format(tc, ans))
