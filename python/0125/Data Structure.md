# Data Structure(데이터 구조)

## 1. String method

immutable(변경 x), iterable(하나씩 반환가능), ordered(순서 있음)

>[String method document](https://docs.python.org/ko/3/library/stdtypes.html#string-methods)

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

mutable(변경 가능), iterable(하나씩 반환가능), ordered(순서 있음)

>[Data structures documet](https://docs.python.org/ko/3/tutorial/datastructures.html#more-on-lists)

- `.append(x)` x값 추가
-  `.extend(x)` x(list, range, tuple, string) 값 추가

```python
test.extend('가나다') -> ['가나다']
test.extend('가나다') -> ['가', '나', '다'] #string 사용시 주의
```

- `.insert(idx, x)` 정해진 위치 idx에 x값을 추가한다
- `.remove(x)` x값을  삭제합니다
- `.pop(idx)` idx위치의 값을 삭제하고, 그 항목 반환 (단, idx 미지정시 마지막항목 선택)
- `clear` 모든 항목 삭제
- `.index(x)` x값을 찾아서 해당 index값 반환 (x값이 존재하지 않으면 에러발생)
- `.count(x)` x값의 갯수를 확인할 수 있다
- `.sort()` 정렬 

```python
numbers = [1,7,2,6,5]
sorted(numbers) # 정렬된 값을 반환한다.
print(numbers) # 출력 [1, 7, 2, 6, 5]
numbers.sort() # 원본을 변경한다.
print(numbers) # 출력 [1, 2, 5, 6, 7]
```

- `.reverse()` 반대로 뒤집는다

### 2.1 List Copy

- Copy시 주의사항

```python
origin = [1,2,5]
copy = origin # 리스트 복사 시 같은 곳을 바라본다(동일 id를 가진다)
copy[1] = '안녕' # 그로인해 복사 리스트값을 변경 할 시 원본값도 변경된다
print(origin, copy) # 출력 [1, '안녕', 5] [1, '안녕', 5]
```

- Copy 방법

```python
origin = [1,2,5]
# 1 [:]를 활용
copy = [:]
# 2 list()를 활용
copy = list(origin)
# 3 deepcopy()를 활용
import copy
copy = copy.deepcopy(origin)
```

>#1과 #2의 방법은 중첩 list를 복사하지는 못한다.

# 3. Built-in Function

iterable 데이터 구조에 적용가능하다.

- `map(function, iterable)`  데이터 구조의 모든요소에 function을 적용하고 그 결과값을 반환
- `filter(function, iterable)`  데이터 구조의 요소 중 function의 반환 결과가 True인것만 반환
- `zip(*iterables)` 복수의 iterable객체를 tuple로 묶어서 반환한다.

## 4. set method

mutable(변경 가능), iterable(하나씩 반환가능), unordered(순서 없음)

> [Set method document](https://docs.python.org/ko/3/library/stdtypes.html#set-types-set-frozenset)

- `.add(x)` x를 추가한다.
- `.update(*x)` 여러가지 값 추가(인자로는 반드시 iterable 구조를 전달)
- `.remove(x)` x를 삭제한다.(x값이 없으면 KeyError발생)
- `.discard(x)` x를 삭제한다(x값이 없어도 에러발생 X)
- `.pop()` 임의의 원소 제거 후 반환

## 5. Dictionary method

mutable(변경 가능), iterable(하나씩 반환가능), unordered(순서 없음)

> [Dict method document](https://docs.python.org/ko/3/library/stdtypes.html#mapping-types-dict)

- `.get(key[, default])` key값에 해당하는 value반환, default값 설정가능(기본은 None)
- `.pop(key[, default])` key값을 삭제하고 해당하는 value반환, default 미설정시 key값이 존재하지않으면 KeyError발생
- `.update()` key : value 덮어쓰기 및 추가

```python
test_dict.update({'name' : '홍길동'})
test_dict.update(name = '홍길동')
```

- `.keys()` key값들을 반환
- `.values()` value값들을 반환
- `.items()` tuple형식으로 (key, value)쌍 반환