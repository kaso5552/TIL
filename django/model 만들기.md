# model 만들기

1. 앱 만들기 단계까지 수행
2. 모델 정의하기
   - 클래스를 이용해서 모델정의(python object로)
   - `class 모델명(models.model)`
     - 필드명 = 필드타입 
   - `python manage.py makemigrations`( migration 파일 생성)
   - `python manage.py migrate` (DB적용)
3. orm을 통해서 데이터 넘기기
   - `python manage.py shell`-> 일일이 import해야해서 불편하다
   - `python manage.py shell_puls` 를 사용하자
     - 확장 프로그램 `pip install django-extensions` 를 깔아야한다.
     - 이후 project `setting`의  `INSTALLED_APPS` 에 `'django_extensions'`를 추가하자
   - article = Articles() <- 정의 하기
   - 값을 넣기
     - `article = Articles(title='second', content='django!!')`
     - `article.title = second`
   - 저장하기 article.save()
   - 또는 `Articles.objects.create(title='third', content='django!!!')` 따로 정의하지않고 바로 만들기

4. admin 만들기

   - `python manage.py createsuperuser`

   - `admin.py` 에 등록하기

     - `from .models import Article`

     - `admin.site.register(Article)`

       