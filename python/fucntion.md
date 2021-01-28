# 나만의 함수정리

## 1. 내부함수

 - 파이썬 내부에 저장되어있어 `함수명`으로 사용가능하다
   	- print()
- `dir(__bulitin__)` 파이썬 내장함수(builtin _in_)를 확인할 수 있다
    - [파이썬 내장함수](https://docs.python.org/ko/3/library/functions.html)
- `abs()` 절대값 함수

```python
print(abs(-5))
#출력
5
```

- `divmod(a, b)` a 값을 b값으로 나눈 몫과 나머지를 출력한다

```python
quotient, remainder = divmod(number, 10) 
# number를 10으로 나눈 몫이 quotient, 나머지가 remainder에 저장된다
```

- `chr()` 숫자를 아스키 코드값의 문자로 변환
- `ord()` 아스키 코드값의 문자를 숫자로 변환

## 2. 외부함수

 - 파이썬 외부에서 불러와서 출력하는 함수 `import 함수명` 을 통해서 사용가능하다 
   	- ex ) `import math`
 - `함수명.함수`를 통해서 사용가능하다
   	- ex ) `math.isclose`
 - `from 함수명 import 함수`를 통해서 함수명 없이 사용가능하다.(내부함수처럼 사용가능)
   	- ex) `form math import isclose` -> `isclose갯수를 영어로초ㅑㅐ`

### keyword

- `kwlist`  keyword함수의 리스트를 출력한다

### sys

- `maxsize`  일반 정수의 최대값 2**63 -1의 값을 나타낸다
- `float_info.epsilon` 반올림 오차의 상한값을 나타낸다

### datetime

 - `datetime` 현재 년-원-일 시:분:초 가 출력이된다

### math

- `isclose(a, b)` a와 b가 근접하면 `True` 아니면 `Fales`를 반환한다

### requests

- `get(주소값)` 해당 주소값의 응답코드를 받는다  

### pprint

- `pprint`  정렬된 print가 가능하다. 주로 많은 양의 정보를 정렬해서 출력할때 사용한다.

### random

- `.sample(x, number)` x에서 중복없이 number만큼 반환
- `.choice(x)` x에서 랜덤값 반환
- `.choice(x, k=number)` x에서 number길이만큼의 리스트 값 반환

```python
a = [1,2,3,4,5]
choice(a, k=2) # 출력 [3,1] ..
```

