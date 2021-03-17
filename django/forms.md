# forms

[forms field](https://docs.djangoproject.com/en/3.1/ref/forms/fields/) [form](https://docs.djangoproject.com/en/3.1/topics/forms/)

- django 프로젝트의 주요 유효성 검사 도구
- 공격 및 데이터 손상에 대한 `중요한` 방어수단
- 폼을 사용하면 양식 처리를 간단하게 할 수 있다

#### 순서

1. `forms.py` 파일 생성 (app의 내부의 생성)

2. class 설정 

   1. ```python
      class ArticleForm(forms.Form):
          title = forms.CharField(max_length=10)
          content = forms.CharField(widget=forms.Textarea)
      ```

   - 보통 app 이름에 form을 설정하거나 model 이름에 폼을 설정한다
   - 위와 같이 직접 폼을 설정 할 수 있다
     - form에는 textfield가 없어서 위와 같이 설정해야한다

   2. ```python
      class ArticleForm(forms.ModelForm):
          class Meta:
              model = Article
              fields = '__all__'
      ```

   - 위와같이 model을 가지고 와서 모든 필드를 한번에 받을 수 있다
   - `form .models import model`명에 주의하자



#### 사용법

- views에서 사용하기전에 import 하자
- 변수명 = 클래스명을 통해 불러올 수 있다
- `form.is_valid()` 유효성 검사를 할 수있다.(보통 if문에 활용)
- 이미 저장된 정보를 불러 올때 `instance=model명` 을 통해 불러온다
- `form.as_p` 를 통해서 필드전체를 불러 올 수 있다.