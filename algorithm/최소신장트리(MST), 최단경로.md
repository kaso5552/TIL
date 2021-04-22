# 최소신장트리(MST)

> 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리



## Prim

> 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST 만들어가는 방식



1. 임의 정점 선택
2. 인접한 정점들 중의 최소 비용의 간선 정점 선택
3. 반복

```python
def prim():
    # 시작점 0으로 세팅
    total = 0
    u = 0 # 시작점을 0으로 설정
    D[u] = 0

    # 정점을 V개 선택
    for i in range(V):
        # 가중치가 최소인 정점을 찾기
        min = 987654321
        for v in range(V):
            if visited[v] == 0 and min > D[v]:
                min = D[v]
                u = v
        # 방문처리
        visited[u] = 1
        total += adj[PI[u]][u]

        # 가중치가 최소인 정점의 인접한 정점들의 가중치 업데이트
        for v in range(V):
            if adj[u][v] != 0 and visited[v] == 0 and adj[u][v] < D[v]:
                D[v] = adj[u][v]
                PI[v] = u

    return total

V, E = map(int,input().split())
adj = [[0] * V for _ in range(V)]

# 초기화 작업
D = [987654321] * V # 가중치를 모두 무한대
PI = list(range(V))       # 내 부모는 나다
visited = [0] * V   # 방문표시

# 입력
for i in range(E):
    edge = list(map(int,input().split()))
    adj[edge[0]][edge[1]] = edge[2]  # 방향성 없음
    adj[edge[1]][edge[0]] = edge[2]  # 방향성 있음

print(prim())
```



## 최단경로

> 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로



## Dijstra

```python
def dijstra(start):
    # 시작점 0으로 세팅
    u = start # 시작점을 start으로 설정
    D[u] = 0

    # 정점을 V개 선택
    for i in range(V):
        # 가중치가 최소인 정점을 찾기
        min = 987654321
        for v in range(V):
            if visited[v] == 0 and min > D[v]:
                min = D[v]
                u = v # 최고값

        # 방문처리
        visited[u] = 1

        # 가중치가 최소인 정점의 인접한 정점들의 가중치 업데이트
        for v in range(V): # u 정점의 인접한 v 정점들
            if adj[u][v] != 0 and visited[v] == 0 and D[v] > D[u] + adj[u][v]:
                D[v] = adj[u][v] + D[u]

V, E = map(int,input().split())
adj = [[0] * V for _ in range(V)]

# 초기화 작업
D = [987654321] * V # 가중치를 모두 무한대
visited = [0] * V   # 방문표시

# 입력
for i in range(E):
    edge = list(map(int,input().split()))
    adj[edge[0]][edge[1]] = edge[2]  # 방향성 없음
    adj[edge[1]][edge[0]] = edge[2]  # 방향성 있음
dijstra(0)
print(D)
```



