import sys
sys.stdin = open('sw_5789_현주의 상자 바꾸기_input.txt','r')

def Remove(l,r,num):
    for i in range(l,r+1):
        ans[i] = num

T = int(input())
for tc in range(1,T+1):
    N, Q = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(Q))
    ans = [0]*(N+1)
    for i in range(len(arr)):
        L = arr[i][0] # 시작값
        R = arr[i][1] # 끝값
        Remove(L, R, i+1)
    print('#{}'.format(tc),end = ' ')
    for i in range(1,N):
        print('{}'.format(ans[i]),end=' ')
    print(ans[-1])