import sys
sys.stdin = open('sw_1232_사칙연산_input.txt', 'r')

def postorder(node):
    if node <= N and num[node] == 0:
            n1 = postorder(fc[node])
            n2 = postorder(sc[node])

            num[node] = cal(n1,n2,operator[node])
    return num[node]

def cal(a,b,o):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a / b

oper = ['+','-','*','/']
T = 10
for tc in range(1,T+1):
    N = int(input())
    operator = [0] * (N+1)
    fc = [0] * (N+1)
    sc = [0] * (N+1)
    num = [0] * (N+1)
    for i in range(N):
        temp = list(input().split())
        l = len(temp)
        p = int(temp[0])
        if temp[1] in oper:
            operator[p] = temp[1]
        else:
            num[p] = int(temp[1])
        if l >= 3 :
            fc[p] = int(temp[2])
            if l == 4:
                sc[p] = int(temp[3])
    postorder(1)
    print('#{} {}'.format(tc,int(num[1])))