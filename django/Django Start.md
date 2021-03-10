# Django Start

> python 으로 만들어진 웹 애플리케이션 프레임워크이다. 쉽고 빠르게 웹사이트를 개발하기 위해서 만들었다

- 소프트웨어 디자인 패턴 `MVC`(Model-View-Controller)을 따른다.
- django는 `MTV`(Model-Template-View)구조로 구성되어있다.
  - Model : 데이터베이스를 관리한다
  - Template : 화면을 관리한다. (html)
  - View : 중앙에서 컨트롤러 역할을 수행(python)
- 기본동작구조 ([참조](https://mdn.mozillademos.org/files/13931/basic-django.png), mdn공식문서)
  - ![기본동작구조](https://mdn.mozillademos.org/files/13931/basic-django.png)

### 가상환경 설정

> 파이썬 환경을 새롭게 다른 공간에 만드는 환경

1. `python -m venv venv` (가상환경 만들기)
2. `source venv/scripts/activate` (가상환경으로 들어가기)

### django project 만들기

1. `django-admin startproject 프로젝트 명`  or `python -m django startproject 프로젝트 명`
2. `cd 프로젝트 명` (해당 폴더로 이동, `manage.py`와 동일한 위치)



### django app 만들기

1. `python manage.py startapp app이름s` (무조건 이름은 복수형으로 설정)
2. project에 `settings.py` 안  `INSTALLED_APPS` 에 등록
3. `language code, time zone` 수정
   - language code : `ko-kr`
   - time zone : `Asia/Seoul`



### 이후 진행

- `python manage.py runserver` (서버 시작)
- `urls.py` -> `views.py` -> `template 파일` 순서로 수정