import sys
sys.stdin = open('sw_5097_회전_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    front, rear = -1, -1
    Q = [0] * 1000
    for i in range(N):
        rear += 1
        Q[rear] = arr[i]
    for i in range(M):
        rear += 1
        Q[rear] = Q[front+1]
        front += 1
    print('#{} {}'.format(tc,Q[front+1]))

