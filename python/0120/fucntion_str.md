# 함수(function)

특정한 기능을 수행하는 코드의 합

	- `return`을 통해 결과값 전달 가능(`return`값이 없으면 `None`을 전달)
	- 오직 한 개의 객체만 반환할수 있다.

## 가변인자

개수가 정해지지 않은 임의의 인자를 받을려면 가변 인자 리스트 `*args`를 활용, `tuple`형태로 처리, 

매개변수에 `*`표시

 - 가변 인자 리스트는 매개변수 목록의 마지막에 위치 

   	- ex ) def fun_test(a, b, *args) :

 - 만약 가변 인자 리스트가 마지막이 아니라면

    - ex ) def fun_test(*args, name) :  

      > def fun_test('철수', '영희', name = '맹구')  와 같이 끝값 직접 설정

## 가변 키워드 인자

정해지지 않은 키워드 인자들은 `dict`형태로 처리, `**kwargs`로 표현, 매개변수에 `**`표시

 - ex ) def fun_test(**kwargs) :

   > def fun_test(name = '철수', age = 26)로 표현 output 은 {'name' : '철수', 'age' : 26}로 표현

## 스코프(scope)

함수는 코드 내부에 공간을 형성

	- 전역 스코프(global scope) : 어디서든 사용 가능
	- 지역 스코프(local scope) : 함수 내부에서만 사용 가능

### LEGB

같은 이름(식별자)가 존재할때 `LEGB` 순서로 찾는다

	1. Local : 정의된 함수(함수 호출 시 ~ 함수 종료시 까지 존재)
 	2. Enclosed : 상위 함수
 	3. Global : 함수 빡의 변수(모듈이 호출된 시점 이후 ~ 종료시 까지 존재)
 	4. Built-in : 파이썬안 내장 함수(파이썬 실행 시 ~)

```python
# test2 함수 기준으로
a = 10 # Global
def test1():
    a = 20 # enclosed
    def test2():
    	b = 20 # Local
```

## 재귀함수

함수 내부에서 자기 자신을 호출 하는 함수

```python
# 팩토리얼 함수
def factor(number):
    if number == 1:
        return 1
    else :
        return number * factor(number-1)
```





