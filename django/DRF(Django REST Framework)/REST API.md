# REST API

## API(Application Programming Interface)

- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
- 프로그래밍을 활용해서 할 수 있는 것



#### Web API

- 웹 어플 개발에서 다른 서비스에 `요청`을 보내고 `응답`을 받기 위해 정의된 명세
- 보통 Open API를 활용한다
  - ex) 구글, 카카오 지도 등



## REST(REpresentational State Transfer)

- 웹 설계 상의 장점을 활용 할 수 있는 아키텍처 방법론
- REST를 따르는 시스템 or API를 `RESTful API`라고 정의함



### URI(Uniform Resource Identifier)

- 통합 자원 식별자

- 인터넷의 자원을 나타내는 유일한 주소

- 자원을 식별하거나 이름을 지정하는 데 사용되는 간단한 문자열

- URL(Uniform Resource Locator)

  - 통합 자원 위치
  - 네트워크 상에 자원(리소스)이 어디 있는지(주소)를 알려주기 위한 약속
  - '웹 주소' or '링크'를 뜻함

- URN(Uniform Resource Name)

  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할 (고유한 이름)

- 설계 주의사항

  - `_` 이 아닌`-`  사용

  - 소문자 사용

  - 파일 확장자 포함 X

  - URN은 비중이 매우적어서 URL 은 URI를 통칭하는 말로 사용하기도 함

    