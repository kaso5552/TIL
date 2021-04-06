import sys
sys.stdin = open('sw_5178_노드의합_input.txt', 'r')

def fun(node):
    if node <= N and tree[node] == 0:
        n1 = fun(2*node)
        if 2*node+1 <= N:
            n2 = fun(2*node+1)
        else:
            n2 = 0
        tree[node] = n1 + n2
    return tree[node]

T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split())
    tree = [0]*(N+1)
    for i in range(M):
        node, num = map(int,input().split())
        tree[node] = num
    a = fun(1)
    print('#{} {}'.format(tc,tree[L]))