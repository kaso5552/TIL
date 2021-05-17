# Django + Vue

- Server(Django)
  - 정보 제공
  - DB와 통신하며 데이터를 CRUD
  - 요청을 보낸 Client에게 정보를 응답
- Client(Vue)
  - 서버에 요청을 보내서 원하는정보를 get
  - 사용자에게 적절한 방식으로 표현



### CORS(Cross-Origin Resource Sharing)

> 다른 출처에서 온 리소스를 공유하는 행위

- 브라우저 보호의 용도
- django에서 제공하는 헤더파일 사용
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)

