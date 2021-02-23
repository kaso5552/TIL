import sys
sys.stdin = open('sw_1219_길찾기_input.txt','r')

def Find(v):
    # 방문한곳 설정
    visit[v] = 1
    for i in range(100):
        # 인접행렬중에 방문안했으면
        if visit[i] == 0 and data[v][i] == 1:
            Find(i)

def Data():
    for i in range(N):
        s, e = arr[2*i], arr[2*i+1]
        data[s][e] = 1

T = 10
for tc in range(1,T+1):
    test, N = map(int,input().split())
    arr = list(map(int,input().split()))
    data = list([0]*100 for _ in range(100))
    visit = [0]*100
    ans = 0
    Data()
    Find(0)

    if visit[99] == 1:
        ans = 1
    print('#{} {}'.format(tc,ans))

