# JS 문법

> `ECMAscript6` 를 따른다,



## 식별자

> 변수를 구분할 수 있는 변수명

- `문자`, `$`, `_`로 시작
- 대소문자 구분, 클래스명 이외에는 모두 소문자



### 카멜 케이스

> 변수, 객체, 함수 -> 두번째 단어의 첫글자부터 대문자



### 파스칼 케이스

> 클래스, 생성자 -> 모든글자의 첫번째 글자 대문자



### 대문자 스네이크 케이스

> 상수(변경될 가능성이 없는 값) -> 모든단어대문자 and 단어 사이에 언더스코어(`_`)



## 변수

|       | 재할당 | 재선언                      |
| ----- | ------ | --------------------------- |
| let   | 가능   | 변수 재선언 불가능          |
| const | 불가능 | 변수 재선언 불가능          |
| var   | 가능   | 변수 재선언 가능 ( 잘안씀 ) |



## 세미콜론

> 선택적 사용가능

- 세미콜론이 없을 경우 자동으로 삽입

## 데이터 타입

JS의 모든 값은 특정한 데이터 타입을 가진다

|          |         타입          |             변수             |               복사                |
| -------- | :-------------------: | :--------------------------: | :-------------------------------: |
| 원시타입 | 객체가 아닌 기본 타입 | 변수에 해당 타입의 값이 저장 | 변수에 복사할 때 실제 값이 복사됨 |
| 참조타입 |  객체 타입의 자료형   | 변수에 객체의 참조 값이 담김 | 변수에 복사할 때 참조 값이 복사됨 |



### Primitive type(원시 타입)

- **숫자(Number)** 
  - 정수, 실수 구분 없는 하나의 숫자 타입
  - 부동소수점 형식을 따름
- **문자열(String)**
  - 텍스트 데이터
  - 작은따음표 or 큰따옴표 모두 가능
  - 템플릿 리터럴(python f-string과 유사함)
    - backtick(``)으로 표현
    - `${expression}` 표현
- **undefined**
  - 변수의 값이 없음을 나타냄
  - 변수 선언 후 값을 할당하지 않으면 자동으로 할당
- **null**
  - 값이 없음을 의도적으로 표현
- **불리언(Boolean)**
  - 논리적 참 또는 거짓을 나타냄
  - true or false
  - 값이 없거나 `0`, `-0`, `null`, `NaN`,`undefined`, 빈 문자열("")이면 `false`



### Reference type(참조 타입)



## 연산자



### 할당 연산자

> 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연선자에 할당하는 연산자

```JS
let x = 0
x += 5 // 5
x -= 1 // 4
x ++ // 5
x -- // 4
```



### 비교 연산자

> 피연산자들을 비교하고 비교의 결과값을 불리언으로 반한화는 연산자



### 동등 비교 연산자(==)

> 두 피연산자가 값은 값인지 불리언 값을 반환하는 연산자

- 암묵적 타입 변환을 통해 일치시킨 후 비교

- 특별한 경우를 제외하고 사용 X



### 일치 비교 연산자(===)

> 두 피연산자가 값은 값인지 불리언 값을 반환하는 연산자

- 엄격한 비교가 이뤄지고 암뭄적 타입변환 X



### 논리 연산자

- and : `&&`
- or : `||`
- not : `!`



### 삼항 연산자

> 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자

- `조건 ? 참값 : 거짓값`



## 조건문



### if statement

```js
if (condition1) { 내용 } 
else if (condition2) { 내용 } 
else { 내용 }
```



### switch statement

> 표현식의 결과값을 이용한 조건문

- 표현식의 결과값과 case 문의 오른쪽 값을 비교
- break, default문은 선택적 사용가능
- break문이 없는 경우 break or default문을 실행할 때까지 조건문 실행

```js
switch (expression) {
    case 'first' : {
        내용
        break
    }
    case 'second' : {
        내용
        break
    }
    default: {
       	내용
    }
}
```



## 반복문



### while

```js
while (condition) {
    내용
}
```



### for

> 세미콜론으로 구분되는 세 부분 으로 구성

- `(초기값 ; 조건 ; 값의 증감) `

```js
for (initialization; condition; expression){
    내용
}
```



### for... in

> 객체의 속성들을 순회할 때 사용

- 배열도 순회가능하지만 권장 X

```js
for (variable in object){
    내용
}
```



### for... of

> 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용

- 배열순회시 사용

```js
const movies = ['반도', '해운대', '해리포터']

for (let movie of fruits) {
    console.log(fruit)
}
```



## 함수



### 선언식

```js
function 함수명 (매개변수) {
    내용
}
// 예시
function add (num1, num2) {
    return num1 + num2
}
```

- 호이스팅(hoisting) 함수 선언식
  - 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting발생
  - 함수 호출 이후에 선언해도 동작
- 

### 표현식

> `표현식`(어떤 하나의 값으로 결정되는 코드 단위) 내에서 함수를 정의

- 이름이 없는 함수(익명 함수)는 함수 표현식에서만 사용 가능

```js
const sub = function (num1, num2) {
    return num1 - num2
}
```

- 기본인자 작성이 가능하다

```js
const sub = function(num1 = 10) {
    console.log(num1)
}
```



### 호이스팅(hoisting)

- 함수 선언식
  - 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting발생
  - 함수 호출 이후에 선언해도 동작



- 함수 표현식
  - 표현식으로 선언한 함수는 hoisting시 에러 발생
    - 함수를 변수에 할당함으로 변수의 scope규칙을 따르기 때문에 발생
  - var로 정의 X



### Arrow Function(화살표 함수)

[화살표 함수]([화살표 함수 - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions))

1. function 키워드 생략 가능 (필수)
2. 매개변수가 단 하나 뿐이면, '()'도 생략가능 (선택)
3. 바디가 표현식 하나라면 ‘{ }’과 return도 생략 가능 (선택)

```js
const arrow = function (name) {
    return `안녕! ${name}`
}

// 1
const arrow = name => {return `안녕! ${name}`}

// 2
const arrow = name => {return `안녕! ${name}`}

// 3
const arrow = name => `안녕! ${name}`
```



## 배열 (Arrays)

>  키와 속성들을 담고 있는 참조 타입의 객체

- 순서를 보장
- 주로 대괄호를 이용해서 생성, 0을포함한 양의 idx로 접근가능
- 배열의 길이는 `array.length` 로 접근가능
- 다양한 method 존재



#### reverse

> 요소들의 순서를 반대로 정렬

- array.reverse()



#### push & pop

> 가장 뒤에 요소를 추가 or 제거

- array.push() : 추가
- array.pop() : 제거



#### unshift & shift

> 가장 앞에 요소를 추가 or 제거

- array.unshift() : 추가
- array.shift() : 제거



#### includes

> 특정 값이 존재하는지 판별 후 참/거짓 반환

- array.includes(value)



#### indexOf

> 특정 값이 존재하는지 판별 후 인덱스 반환

- 요소가 없을 경우 -1 반환
- array.indexOf(value)



#### join

> 모든 요소를 구분자를 이용하여 연결

- array.join(seperator(구분자))



### callback 함수

> 어떤 함수의 내부에서 실행될 목적으로 `인자로 넘겨받는 함수`

- 함수가 인자로 전달된다.



#### forEach

> 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

- 3가지 매개변수로 구성
  - element : 배열의 요소 (필수)
  - index : 배열 요소의 인덱스 (선택)
  - array : 배열 자체 (선택)
- `return이 없는 method`

```js
array.forEach(element, index, array) => {
    내용
}



#### map

> 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

```js
array.map((element, index, array) => {
    내용
})
```





#### filter

> 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

```js
const number = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index) => {
    return num % 2
})

console.log(oddNums) // 1, 3, 5
```



#### reduce

> 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

- acc : 이전 콜백 함수의 반환 값이 누적되는 변수
- initialValue : 최초 콜백 함수 호출 시 acc에 할당되는 값, 설정가능하고 직접 제공하지 않으면 배열의 첫번째 값 사용

```js
array.reduce((acc, element, index, array) => {
    내용
}, initialValue)
```



#### find

> 반환 값이 참이면 해당 요소를 반환



#### some

> 요소 중 하나라도 판별 함수를 통과하면 참을 반환



#### every

> 모든 요소가 판별 함수를 통과하면 참을 반환



## 객체(Object)

속성의 집합이면 중괄호 내부에 key와 value의 쌍으로 표현

- key는 문자열 타입
- value는 모든타입
- 접근은 점 or 대괄호



### js만의 객체 문법



### 1. 속성명 축약

> key와 할당하는 변수의 이름이 같으면 축약 가능

```js
let movies = ['반도', '해운대']
let books = '로빈슨쿠르소'

const hobby = {
    movies : movies,
    books : books,
}

// key와 할당하는 변수의 이름이 같으면 축약 가능
const hobby = {
    movies,
    books,
}
```



### 2. 매서드명 축약

> 매서드(어떤 객체의 속성이 참조하는 함수) 선언시 function 키워드 생략 가능

```js
const test = {
    tests, function () {
        console.log('안녕')
    }
}

// 매서드(어떤 객체의 속성이 참조하는 함수) 선언시 function 키워드 생략 가능
const test = {
    tests() {
        console.log('안녕')
    }
}
```



### 3. 계산된 속성

> 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

[mdn 문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Object_initializer#%EA%B3%84%EC%82%B0%EB%90%9C_%EC%86%8D%EC%84%B1%EB%AA%85)

```js
// 계산된 속성명
let i = 0
let a = {
  ["foo" + ++i]: i,
  ["foo" + ++i]: i,
  ["foo" + ++i]: i
}

console.log(a.foo1) // 1
console.log(a.foo2) // 2
console.log(a.foo3) // 3
```



### 4. 구조 분해 할당

> 배열 또는 객체를 분해하여 `속성을 변수에 쉽게 할당`할 수 있는 문법

```js
const hobby = {
    movie : '해운대',
    book : '로빈슨쿠르소',
    game : 'LOL',
}

const movie = hobby.movies
const book = hobby.books

// 구조 분해 할당
const {movie} = hobby
const {book} = hobby

const {movie, book} = hobby
```



### JSON (JavaScript Object Notation)

> key-value쌍의 형태로 데이터를 표기하는 언어

- `JSON.parse()` : `JSON -> 객체`
- `JSON.stringify()` : `객체 -> JSON`