# Backtracking(백트래킹)

해를 찾아가면서 (해가 아니면) 되돌아가서 다시 검색

- 보통 최적화,결정 문제에서 사용
  - ex) 미로찾기, subset sum 등

### Powerset(부분집합)

```python
# {2, 5, 7} 부분집합
arr = [2, 5, 7]
N = len(arr)
A = [0] * N # 원소의 포함 여부를 저장

def powerset(n, k): # n : 원소의 갯수, k = 현재 depth
    if n == k:
        # 솔루션 구하기
        for i in range(len(A)):
            if A[i]:
                print(arr[i],end=' ')
        print()
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k + 1)


powerset(N, 0)
```

- 출력

```
2 5 7 
2 5 
2 7 
2 
5 7 
5 
7 
```



