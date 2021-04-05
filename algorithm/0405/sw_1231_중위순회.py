import sys
sys.stdin = open('sw_1231_중위순회_input.txt', 'r')

def inorder(node):
    if node != 0:
        inorder(fc[node])
        result.append(alpha[node])
        inorder(sc[node])

T = 10
for tc in range(1,T+1):
    N = int(input())
    alpha = ['0'] * (N+1)
    fc = [0] * (N + 1)
    sc = [0] * (N + 1)
    result = []
    for i in range(1,N+1):
        temp = list(input().split())
        address = int(temp[0])
        alpha[i] = temp[1]
        if address * 2 <= N:
            fc[i] = int(temp[2])
            if address * 2 + 1 <= N:
                sc[i] = int(temp[3])
    inorder(1)
    print('#{}'.format(tc),end=' ')
    print(''.join(result))