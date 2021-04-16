import sys
sys.stdin = open('sw_1970_거스름돈_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    M = int(input())
    bills = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * 8
    while M >= 10:
        for i in range(8):
            ans[i] = M // bills[i]
            M %= bills[i]
    print('#{}'.format(tc))
    print(*ans)
