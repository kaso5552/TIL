# Vue.js

> 사용자 인터페이스를 만들기 위한 프로그레시브 프레임워크

- SPA(Single Page Aplication)를 완벽하게 지원
  - 현대 페이지를 동적으로 작성함으로써 사용자와 소통하는 웹 어플
  - 서버로부터 처음에만 페이지를 받아오고 이후에는 동적으로 dom을 구성
    - 연속되는 페이지 간의 사용자 경험을 향상
- CSR(Client Side Rendering)
  - 최초 요청 시 서버에서 빈 문서 응답 -> 클라이언트에서 데이터를 요청 -> 데이터를 받아 DOM을 렌더링

- MVVM Pattern
  - Model
    - JS의 object 자료구조
    - 내부에서 data로 사용되며 값이 변경될시 View(DOM)이 반응
  - View
    - DOM(HTML)
    - data의 변화에 따라서 바뀌는 대상
  - ViewModel
    - 모든 vue instance
    - viewdhk model 사이에서 data,DOM에 관련된 일을 처리



## Vue Instance

