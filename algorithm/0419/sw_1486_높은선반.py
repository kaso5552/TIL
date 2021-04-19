import sys
sys.stdin = open('sw_1486_높은선반_input.txt', 'r')

def search(n, s):
    if s >= B:
        ans.add(s-B)
    if n == N:
        return 0
    else:
        search(n+1, s+H[n])
        search(n+1, s)


T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))
    H = sorted(H)
    ans = set()
    search(0, 0)
    print('#{} {}'.format(tc,min(ans)))
