import sys
sys.stdin = open('sw_5176_이진탐색_input.txt', 'r')

def inorder(node):
    global count
    if node <= N:
        inorder(2*node)
        tree[node] = count
        count += 1
        inorder(2*node+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    count = 1
    inorder(1)
    print('#{} {} {}'.format(tc,tree[1],tree[N//2]))