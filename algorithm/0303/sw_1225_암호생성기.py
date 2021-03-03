import sys
sys.stdin = open('sw_1225_암호생성기_input.txt', 'r')
import collections


T = 10
for tc in range(1,T+1):
    test_case = int(input())
    arr = list(map(int,input().split()))
    deq = collections.deque()
    for i in range(8):
        deq.append(arr[i])
    count = 0
    while True:
        for i in range(1,6):
            data = deq.popleft()
            if data - i > 0:
                deq.append(data-i)
            elif data - i <= 0:
                deq.append(0)
                count = 1
                break
        if count == 1:
            break
    print('#{}'.format(tc),end=' ')
    print(*deq)

