# 나만의 함수정리

## 1. 내부함수

 - 파이썬 내부에 저장되어있어 `함수명`으로 사용가능하다
   	- print()

### Sequence형에서 자주사용하는 함수

	- `.count(x)` x의 개수를 나타낸다. 

### non-Sequence형에서 자주사용하는 함수

#### dictionary

	- `.keys()`  key값을 확인할 수 있다
	- `.values()`  value값을 확인할 수 있다
	- `.items() `  key, value값을 모두 확인할 수 있다

## 2. 외부함수

 - 파이썬 외부에서 불러와서 출력하는 함수 `import 함수명` 을 통해서 사용가능하다 
   	- ex ) `import math`
 - `함수명.함수`를 통해서 사용가능하다
   	- ex ) `math.isclose`
 - `from 함수명 import 함수`를 통해서 함수명 없이 사용가능하다.(내부함수처럼 사용가능)
   	- ex) `form math import isclose` -> `isclose`

### keyword

	- `kwlist`  keyword함수의 리스트를 출력한다

### sys

	- `maxsize`  일반 정수의 최대값 2**63 -1의 값을 나타낸다
	- `float_info.epsilon` 반올림 오차의 상한값을 나타낸다

### datetime

 - `datetime` 현재 년-원-일 시:분:초 가 출력이된다

### math

	-  `isclose(a, b)` a와 b가 근접하면 `True` 아니면 `Fales`를 반환한다

### requests

	- `get(주소값)` 해당 주소값의 응답코드를 받는다  

### pprint

	- `pprint`  정렬된 print가 가능하다. 주로 많은 양의 정보를 정렬해서 출력할때 사용한다.

