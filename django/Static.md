# Static

[static files](https://docs.djangoproject.com/en/3.1/howto/static-files/#managing-static-files-e-g-images-javascript-css)

> image, css, js 파일과 같이 내용이 고정되어, 응답시 파일 내용을 그대로 보여주면 되는 파일
>
> 보통 개발자가 준비하는 파일

- 기본 static 경로 : `app_name/static/`
- 기본 작성법

```django
{% load static %}
<img src="{% static 'app_name/sample.jpg' %}" alt="sample">
```

- STATIC_ROOT
  - collectstatic이 배포를 위해 정적 파일을 수집하는 절대경로
  - collectstatic : 프로젝트 배포 시 흩어져 있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
  - settings에 `STATIC_ROOT = "경로"`로 설정한다
  - `python manage.py collectstatic` 명령어 사용
- STATIC_URL
- 

스태틱은 개발자가 준비하는 파일(css, js, img)

미디어 파일은 유저가 업로드 하는 파일

​	 enctype="multipart/form-data" 작업

