import sys
sys.stdin = open('sw_5177_이진힙_input.txt', 'r')

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    c = heapcount
    p = heapcount//2

    while p != 0 and heap[p] > heap[c] :
        heap[p], heap[c] = heap[c], heap[p]

        c = p
        p = c//2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    temp = list(map(int,input().split()))
    heap = [0] * (N+1)
    heapcount= 0

    for i in range(N):
        heappush(temp[i])

    ans_count = N
    ans = 0
    while ans_count != 0:
        ans_count = ans_count // 2
        ans += heap[ans_count]

    print('#{} {}'.format(tc,ans))

