import sys
sys.stdin = open('sw_11764_컨테이너운반_input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    weight = list(map(int,input().split()))
    volume = list(map(int,input().split()))
    ans = 0
    for i in range(len(volume)):
        cw = 0
        for j in range(len(weight)):
            if volume[i] >= weight[j]:
                if cw < weight[j]:
                    cw = weight[j]
        ans += cw
        if cw != 0:
            weight.remove(cw)
    print('#{} {}'.format(tc,ans))