import sys
sys.stdin = open('sw_1258_행렬찾기_input.txt', 'r')

def Fution():
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                x, y = 1, 1
                while True:
                    if i + x == N or arr[i+x][j] == 0:
                        break
                    else: x+= 1
                while True:
                    if j + y == N or arr[i][j+y] == 0:
                        break
                    else: y+= 1
                for k in range(i,i+x):
                    for w in range(j,j+y):
                        arr[k][w] = 0
                Q.append((x*y,x,y))

def align():
    for i in range(len(Q)-1):
        for j in range(i,len(Q)):
            if Q[i][0] > Q[j][0]:
                Q[i], Q[j] = Q[j], Q[i]
            elif Q[i][0] == Q[j][0] :
                if Q[i][1] > Q[j][1]:
                    Q[i], Q[j] = Q[j], Q[i]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(list(map(int,input().split())) for _ in range(N))
    Q = []
    Fution()
    align()
    print('#{}'.format(tc),end=' ')
    print('{}'.format(len(Q)),end=' ')
    for i in range(len(Q)-1):
        print('{} {}'.format(Q[i][1],Q[i][2]), end=' ')
    print('{} {}'.format(Q[-1][1],Q[-1][2]))




