# 나만의 에러(Error) 정리

## Syntax Error (문법 에러)

```python
# SyntaxError: invalid syntax 발생 (: 부재)
for i in range(0,2)
	print(i)

# SyntaxError: EOL while scanning string literal (' 부재)
print('안녕하세요)

# SyntaxError: unexpected EOF while parsing ( )가 부재 )
print('안녕하세요'
```



## Exception Error(예외 에러)

```python
# ZeroDivisionError: division by zero (0으로 나눌수 없기 때문에 발생)
1 / 0

# NameError: name 'test' is not defined (test라는 정의된 변수를 호출했기 때문에 발생)
print(test)

#TypeError: unsupported operand type(s) for +: 'float' and 'str'(타입이 잘못되었을경우)
test = 3.5 + 'a'
```



## Exception Handling (예외 처리)

```python
# try & except 구문 # except는 여러구문 가능
try :
    test = int(input())
    print(test/0) # 여기서 ZeroDivisionError 발생
except ZeroDivisionError: # except구문 실행
    print('0으로 못나눈다')
    
# try & except + as 구문
try :
    test = int(input())
    print(test/0)
except ZeroDivisionError as error: # as error를 통해서 에러 메세지 출력
    print(f'{error}가 발생') # 출력 division by zero가 발생
    
# try & except & finally 구문
try :
    test = int(input())
    print(test/0) # 여기서 ZeroDivisionError 발생
except ZeroDivisionError: # except구문 실행
    print('0으로 못나눈다')
finally :
    print(f'에러발생해도 {test}값을 출력해야해') # 에러가 발생하더라도 finally구문은 무조건 실행된다
```

## Exception Raising(예외 발생 시키기)

`raise`를 통해 예외발생 가능

```python
# 임의로 예외를 발생시켜서 메세지를 전달할 수 있다
def test(n):
    return 100 / n
print(test(0))
# 실행시 : ZeroDivisionError: division by zero 발생
# raise를 사용하면
def test(n):
    if n == 0:
        raise ZeroDivisionError('0으로 못나눠요')
    return 100 / n
print(test(0))
# 실행시 : ZeroDivisionError: 0으로 못나눠요 발생
```



