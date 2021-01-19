# API 시스템

## 정의 

애플리케이션 소프트웨어를 구축하고 통합하기 위한 정의 (Application Programming Interface) 

프로그램들이 서로 상호작용하는 것을 도와주는 매개체

## 역할

	1. API는 서버와 데이터베이스에 대한 출입구 역할을 한다.
 	2. API는 어플리케이션과 기기가 원활하게 통신할 수 있도록 한다.
 	3. API는 모든 접속을 표준화 한다.

## 기본순서

	1. **공공데이터포털 회원가입 / 로그인**
 	2. **오픈 API 찾기**
 	3. **오픈 API 신청하기**
 	4. **키 값, 참고문서 얻어오기**
 	5. **VScode, PyCharm 등에서 원하는 값을 출력해본다**

## 파이썬 코딩

```python
import requests
url = '주소값'
# 주소값을 응답을 불러오는데 http문서들은 보통 json()형으로 구성되어있다 
result = requests.get(url).json()
# 많은 양의 주소들을 출력해서 원하는 정보를 담아온다
print(result)

```

