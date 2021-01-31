# python 기본복습

- overflow : 기대했던 값이 출력되지 않는 현상, 메모리가 차고넘쳐흐르는 현상
- 임의 정밀도 산술 : 유동적으로 메모리 운용

- 수 비교하는 방법 

  1. round
  2. abs()
  3. sys.float_info.epsilon
  4. math.isclose

- complex 표현 

  - `.real` , `.imag`

- 이스케이프 시퀀스

  | \0   | NULL           |
  | :--- | -------------- |
  | \t   | 탭             |
  | \r   | 커서초기위치로 |

- 시간표현

```python
from datetime import datetime
test = datetime.now()
print(test)
# 출력 2021-01-31 13:52:42.107445
print(f'{test:%y}년 {test:%m}월 {test:%y}일 {test:%a}, {test:%A} ')
# 출력 21년 01월 21일 Sun, Sunday
```

- `None ` : 없음 값 표현
- 단축평가
  - a and b : a가 거짓이면 a리턴, 참이면 b리턴 
  - True and True만 True이다.
  - 첫번 째 값이 True이면 두번 째 값 확인 후 출력
  - 첫번 째 값이 False이면 첫번 째 값 출력(False 출력)

```python
'가' and '나' -> '나'
0 and '가' -> 0
('가' and '나') in '나다' -> True 
```

- - a or b : a가 참이면 a리턴, 거짓이면 b리턴
  - 둘중 하나만 True여도 True이다
  - 첫번 쨰 값이 False면 두번째 값 확인 후출력
  - 첫번 쨰 값이 True면 첫번 쨰 값 출력(True출력)

```python
'가' or '나' -> '가'
0 or '가' -> '가'
('가' or '나') in '나다' -> False
```

- 연산자 우선순위
  1. ()
  2. Slicing
  3. indexing
  4. **
  5. 음수/양수 부호 +, -
  6. *,  /,  %
  7. +, -
  8. 비교연산자
  9. not
  10. and
  11. or
- container

|              | list    | tuple     | range     | string    | set        | dict    |
| ------------ | ------- | --------- | --------- | --------- | ---------- | ------- |
| 순서(order)  | O(Seq)  | O         | O         | O         | X(non-seq) | X       |
| 수정가능여부 | mutable | immutable | immutable | immutable | mutable    | mutable |

- squence vs non-squence
  - sequence형 특징 : 순서를 가질 수 있다, idx를 사용할 수 있다(특정위치 지정가능)

- 조건표현식

```python
True if 조건식 else False
```

- `enumerate()` 열거 객체를 돌려줌 (idx를 돌려준다) -> tuple형식

```python
test = ['1번','2번','3번','4번']
print(list(enumerate(test,1)))
# 출력 [(1, '1번'), (2, '2번'), (3, '3번'), (4, '4번')]
```

- 가변인자 처리(매개변수 마지막에 `*`처리) -> tuple로 처리

```python
func(a,b,*args)
```

- 키워드인자처리(매개변수 마지막에 `**`처리) -> dict로 처리

```python
func(a,b,**kwargs)
```

- 탐색순서 (LEGB)
  - local scope
  - enclosed scope
  - global scope
  - built-in scope
- 리스트 복사방법

```python
# 1
a = [1,2,3]
b = a[:]
# 2
b = list(a)
# 3
from copy import deepcopy
b = deepcopy(a)
```

- list comprehension (+조건문)

```python
expression for i in iterable
expression for i in iterable if 조건문
expression if 조건문 else for i in iterable
```

- 객체지향 프로그래밍의 장점
  - 코드의 직관성
  - 활용의 용의성
  - 변경의 유연성

 