import sys
sys.stdin = open('sw_5174_subtree_input.txt', 'r')

def preorder(node):
    global ans
    if node != 0:
        ans += 1
        preorder(child[node][0])
        preorder(child[node][1])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    temp = list(map(int,input().split()))
    child = list([0]*2 for _ in range(E+2))
    for i in range(E):
        p = temp[i*2]
        c = temp[i*2+1]
        if child[p][0] == 0:
            child[p][0] = c
        else:
            child[p][1] = c
    ans = 0
    preorder(N)
    print('#{} {}'.format(tc,ans))