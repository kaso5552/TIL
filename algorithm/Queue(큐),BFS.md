# Queue(큐)

stack과 비슷하게 삽입과 삭제의 위치가 제한적인 자료구조

- FIFO(선입선출구조) First In First Out

- 연산

  - `front` : 첫 번째 원소의 idx, `rear` : 마지막 원소의 idx
  - enQueue(item) : 원소 삽입 ( 마지막 원소 뒤에)

  ```python
  def enQueue(item):
  	global rear
  	rear += 1
  	Q[rear] = item
  ```

  - deQueue() : 원소 삭제 ( 가장 앞에 있는 원소)

  ```python
  def deQueue():
  	global front
      front += 1
      return Q[front]
  ```

  - isEmpty() : 공백상태 검사

  ```python
  def isEmpty():
  	return front == rear
  ```

  - isFull() : 포화상태 검사

  ```python
  def isFull():
  	return rear = len(Q)-1
  ```

  - Qpeek(): 가장앞에 있는 원소 반환

  ```python
  def Qpeek():
  	return Q[front+1]
  ```

- 선형 큐의 경우 크기가 한정
- 원형 큐 방식을 활용해 개선가능

- 속도개선을 위해서 deque 사용가능 (원하는곳에서 자유롭게 입출력가능)
  - [colletions deque](https://docs.python.org/ko/3/library/collections.html#collections.deque)



# BFS(Breadth First Search)

- 너비 우선 탐색
- 인접한 정점들을 먼저 방문 후 , 차례로 방문
- 선입선출 형태

```python
def BFS(G, v) : # 그래프 G, 탐색 시작점 v
    Q.append(v) # 시작정점 v를 enQueue
    visited[v] = 1 # 방문한 것으로 표시
    print(v, end=' ')

    while len(Q) != 0: # 큐가 비어있지 않은 경우
        t = Q.pop(0) # deQueue(왼쪽 원소 반환)
        for w in range(1,V+1): # t와 인접한 모드 정점 w에 대해서, w:자식
            if adj[t][w] == 1 and  visited[w] == 0: # w가 not visited이면
                Q.append(w)
                visited[w] = visited[t] + 1
                print(w,end = ' ')
```

- 탐색시작점으로 부터 얼마나 떨어져 있는지 확인 가능
- 재귀 사용이 불가능 , 즉 dfs보다 빠르다

