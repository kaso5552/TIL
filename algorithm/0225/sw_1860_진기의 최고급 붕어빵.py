import sys
sys.stdin = open('sw_1860_진기의 최고급 붕어빵_input.txt','r')

def Bread():
    total_bread = 0
    count = -1
    max_count = arr[0]
    for i in range(len(arr)):
        if max_count < arr[i]:
            max_count = arr[i]
    while True:
        count += 1
        if count % M == 0 and count != 0:
            total_bread += K
        for i in range(len(arr)):
            if count == arr[i]:
                if total_bread == 0 :
                    return 'Impossible'
                else:
                    total_bread -= 1
        if count == max_count:
            return 'Possible'
T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = Bread()
    print('#{} {}'.format(tc,ans))