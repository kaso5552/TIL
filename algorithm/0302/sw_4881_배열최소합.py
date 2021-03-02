import sys
sys.stdin = open('sw_4881_배열최소합_input.txt','r')

def Sum(data,k):
    global result
    if k == N:
        if result > sum(ans):
            result = sum(ans)
    elif result < sum(ans):
        return
    else:
        for i in range(N):
            if check[i] == 0:
                ans.append(data[i])

                check[i] = 1
                Sum(arr[k+1],k+1)
                check[i] = 0
                ans.pop()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int,input().split())) for _ in range(N))
    arr.append(0)
    ans = []
    check = [0] * N
    result = 99999999999999
    Sum(arr[0],0)

    print('#{} {}'.format(tc,result))
