import sys
sys.stdin = open('sw_4408_자기 방으로 돌아가기_input.txt','r')

def Funtion():
    for i in range(N):
        s, e = arr[i][0] , arr[i][1]
        if s > e :
            s, e = e, s
        for i in range((s+1)//2,(e+1)//2+1):
            visited[i] += 1
    return max(visited)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(list(map(int,input().split())) for _ in range(N))
    visited = [0] * 201
    ans = Funtion()
    print('#{} {}'.format(tc,ans))