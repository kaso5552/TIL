import sys
sys.stdin = open('sw_1859_백만장자프로젝트_input.txt','r')

def Sell(n):
    # 재귀탈출
    if n >= len(arr) - 1:
        return 0
    global ans
    max_idx = n
    # 최대값찾기
    max_price = arr[n]
    for i in range(n,len(arr)):
        if arr[i] > max_price:
            max_idx = i
            max_price = arr[i]
    # 이득보기
    for i in range(n,max_idx):
        if arr[i] < max_price:
            ans += max_price-arr[i]
    # 재귀돌리기
    Sell(max_idx+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    Sell(0)
    print('#{} {}'.format(tc,ans))
