# Object Oriented Programming

## (객체 지향 프로그래밍)

컴퓨터 프로그래밍의 패러다임 중 하나로 프로그램을 '객체'들의 모임으로 파악하는 패러다임

[OOP document](https://docs.python.org/ko/3/tutorial/classes.html)

- 코드의 ==직관성==, 활용의 ==용이성==, 변경의 ==유연성==이 뛰어나다.

## Object(객체)

고유 attribute를 가지고 클래스에서 정의한 행위를 수행한다.

>type(타입) : 공통된 attribute(속성)과 method(조작)을 가진 객체들의 분류
>
>attribute(속성) : object의 상태/데이터
>
>method(조작법) : 객체에 적용할 수 있는 행위, class객체 안의 함수



### Type <-> Instance

>instance(인스턴스) : 특정 타입의 실제 데이터 예시

```python
a = 10 # a는 개체, a는 int type의 instance
```

- `isinstance(a, int)`검사 가능 => 상속 관계에 있어도 True
- `type(a) is int`검사 가능 => 해당 클래스인 경우만 True
- `.mro()` method를 가져오는 순서 => 이를 통해서 부모,자식 class유추(확인?)가능



### Attribute <-> method

```python
# Attribute <객체>.<속성>으로 사용
complex의 .real , .imag 등

# method <객체>.<조작법>()으로 사용
list의 sort() 등
```



### Class(클래스)

object들의 분류를 정의

```python
# 다음과 같이 정의, 반드시 Uppercamelcase사용(각 합성어의 첫 글자만 대문자로 표기)
class ClassName :
	...
```



### 정리

```python
class Archer: # class 정의
	
	def double_attack(self): # method 정의
		#...
        
the_god_of_lightning = Archer() # the_god_of_lightning는 instance 정의
```

## OOP Details

### instance & class variable(변수)

```python
class Archer: 
	job_class = 'bow' # class 변수
    
	def __init__(self, name): 
		self.name = name # 인스턴스 변수를 정의 및 할당
        #...
        
the_god = Archer('light') 
the_god.name # 출력 : ligth => 인스턴스 변수
Archer.job_class # 출력 : 'bow' => class 변수
# 인스턴스 변수에서 => 클래스 변수 접근 가능
the_god.job_class # 출력 : 'bow'
# 단, 클래스 변수 재할당 시
the_god.job_class = 'arrow' # job_class라는 새로운 인스턴스 변수 생성
# 원본 클래스 변수 job_class값은 변하지 않는다.
```



### method

> 세종류로 구성이 된다. 각각의 method에 침범하지 않는다.

#### instance method

>클래스 내부에 정의되는 메서드의 기본 값
>
>첫 번째 인자로 자기자신 `self`전달

#### class method

>`@classmethod`데코레이터를 이용해 정의
>
>첫 번째 인자로 클래스 `cls`전달 

#### static method

> `@staticmethod`데코레이터를 이용해 정의
>
> 어떠한 인자도 전달X

```python
class Test:
	def instance(self):
		return self
    
    @classmethod
	def class_met(cls):
		return cls
    
    @staticmethod
	def static(arg): # static method만 첫 번째 인자를 자동으로 넘겨주지 않는다.
        return arg # 따라서 인자 값을 무조건 설정해야 한다.
```



## Inheritance(상속)

> 클래스 상속을 통해서 코드 재사용성을 높일 수 있다. (다중 상속도 가능)

```python
class Archer: # 부모 클래스
    
    def __init__(self, name):
        self.name = name
        #...

class BowMaster(Archer): # 자식 클래스
    
    def __init__(self, name, level):
        super().__init__(name) # super()를 통해서 부모 class 내용 사용가능
    #...

the_god = BowMaster()
```

