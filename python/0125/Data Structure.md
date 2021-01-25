# Data Structure(데이터 구조)

## 1. String method

immutable(변경 x), iterable(하나씩 반환가능), ordered(순서 있음)

- `.find(x)` x의 `첫 번째 위치` 반환, 없으면 `-1` 반환 
- `.index(x)` x의 `첫 번째 위치` 반환, 없으면 오류 발생 
- `.replace(old, new[, count])` old값을 new값으로 변경함, count지정 시 갯수만큼 시행
- `.strip([chars])` char을 지정하면 양쪽에서 제거, char지정 안할 시 공백 제거
  - `.lstrip()` 왼쪽에서 제거, `.rstrip()` 오른쪽에서 제거
- `.split()` 특정한 단위로 나누어 리스트 반환, 기본은 공백

```python
name = '김철수 홍길동 이순신'
print(name.split(' '))
# 출력
['김철수', '홍길동', '이순신']
```

	- `separator.join(x)`  x의 요소들을 separator로 합쳐 문자열 반환

```python
test = ['홍길동', '26']
print('age'.join(test))
# 출력
'홍길동age26'
```

	- `.capitalize()` 앞글자 대문자 변환
	- `.title()` 특정조건 (공백 등)에서만 대문자 변환
	- `.upper()`  모두 대문자 변환
	- `.lower()`  모두 소문자 변환
	- `.swapcase()` 대 -> 소, 소 -> 대로 변환

## 2. List method

mutable(변경 o), iterable(하나씩 반환가능), ordered(순서 있음)

	- `.append(x)` x값 추가
	- `.extend(x)` x(list, range, tuple, string) 값 추가

```python
test.extend(['가나다']) -> ['가나다']
test.extend('가나다') -> ['가', '나', '다'] #string 사용시 주의
```

	- `.insert(idx, x)` 정해진 위치 idx에 x값을 추가한다