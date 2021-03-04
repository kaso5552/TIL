import sys
sys.stdin = open('sw_5102_노드의거리_input.txt', 'r')

def Dfs(s): # s
    Q.append(s)
    visited[s] += 1

    while len(Q) != 0:
        t = Q.pop(0)
        for i in range(1,V+1):
            if visited[i] == 0 and arr[t][i] == 1 :
                Q.append(i)
                visited[i] = visited[t] + 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    arr = list([0]*(V+1) for _ in range(V+1))
    for i in range(E):
        s, e = map(int,input().split())
        arr[s][e] = 1
        arr[e][s] = 1
    visited = [0] * (V+1)
    Q = []
    start, end = map(int,input().split())
    Dfs(start)
    ans = visited[end] -1 if visited[end] != 0 else 0
    print('#{} {}'.format(tc,ans))