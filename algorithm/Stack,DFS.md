# Stack

- 자료를 쌓아 올린 형태의 구조
  - 선형구조 : 1대 1의 관계
  - 비선형구조 : 1대 N의 관계
- 후입선출`LIFO(Last In Fisrt Out)`



# DFS(Depth Fisrt Search)

- 깊이 우선 탐색
- 모든 정점을 방문하는 순회방법
- 후입선출의 구조

#### 알고리즘

1.  시작 정점 v를 방문
2.  정점 v에 인접한 정점들을 확인
   - 방문하지 않은 정점이 있으면 stack에 push 이후 정점 w 방문, w->v 로해서 알고리즘 반복
   - 방문하지 않은 정점이 없으면, 스택을 pop하여 마지막 방문 정점으로 돌아간다
3. 스택이 공백이 아니라면 2번 반복

```python
def DFS(v): # v : 시작정점
    # visited체크
    visited[v] = 1 # 전역에 visited = [0] * (V+1)을 만들어놓았다 
    # v의 인접한 정점(w) 찾기
    for w in range(1,V+1): # V : 정점의 갯수 
        if arr[v][w] == 1 and visited[w] == 0: # arr은 v->w로 가는 노선이 있는이 없는지 여부판별
            DFS(w) # 반복하기
```



