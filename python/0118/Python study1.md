# Python 공부

## 기초 문법

### 1. 변수

#### 1-1식별자

 - 식별자는 변수, 함수 등 식별하데 사용하는 이름이다.
 - 사용불가 키워드

```python
import keyword
print(keyword.kwilst)
```

```False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield```



### 2.컨테이너

여러 개의 값을 저장하는 것

	- 시퀀스형 : 순서가 있는 데이터
	- 비 시퀀스형 : 순서가 없는 데이터

#### 2-1 시퀀스형

 - `list` 대괄호 [] 및 list()를 통해 생성가능

 - ` tuple` ()로 생성, `수정 불가능(immutable)` 하다

 - `range`  range(n, m, s)로 표현 n부터 m-1까지 +s만큼 증가, n과 s는 생략가능 하며 n=0, s=1이 기본값이다, 

   `수정 불가능(immutable)`이다

- `string` '' 를 통해서 생성, `수정 불가능(immutable)`이다

#### 2-2 비 시퀀스형

 - `set` {}를 통해서 생성, 순서가 없고 중복된 값이 없다
    - 빈 집합 만들기 `set_a = set()`
    - set 연산
       - 합집합 `set_a | set_b`
       - 교집합 `set_a & set_b`
       - 차집합 `set_a - set_b`
 - `dictionary` {}를 통해서 만들고, dict()로도 생성가능하다. `key`는 수정불가능 이며 `value`는 수정가능하다.
    - 기본구조 `{key : value}`

### 3. 제어문

	- 조건 표현식 `num1 if <조건식> else num2` 로 표현하며 조건식이 참이면  `num1`  거짓이면 `num2`를 출력









