# Authentication system(인증 시스템)

기본적인 built-in form 제공 

- `UserCreationForm`(회원가입)
- `AuthenticationForm`(로그인)
- `UserChangeForm`(회원정보수정)

## accounts

보통 로그인 시스템은 accounts app 에서 진행한다.

- `is_authenticated` attribute : 회원인지 아닌지 판별 -> 회원이면 True 아니면 False

  - 이미 로그인해있거나 회원가입이 필요없을 경우 if 문을 활용해서 전 위치로 돌려보내는데 이용

- ```python
  from django.contrib.auth.decorators import login_required
  
  @login_required
  def ... 
  ```

> 로그인 상태일때만 함수동작이 가능하게 설정하는 구문이다

#### 회원가입(Signup)

##### signup 함수

```python
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm() # 회원가입 form , 장고에서 제공해준다
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)
```

- `UserCreationForm()` : 장고에서 제공해주는 회원가입 form
- `user = form.save()` : `request.POST`에서 담겨온 정보를 저장한다. 그리고 return값으로 user정보를 반환한다,
- `auth_login(request, user)` : user정보를 바탕으로 로그인을 진행한다.

##### signup.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>회원가입</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock %}
```



#### 로그인(Login)

##### login함수

```python
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```

- `AuthenticationForm` 을 활용해서 정보를 받아와서 
- `auth_login(request, form.get_user())` 를 통해서 로그인한다.

##### login.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>로그인</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock %}
```



#### 회원탈퇴(Delete)

##### delete함수

```python
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
```

- `request.user.delete()` request에 담겨온 user정보를 삭제한다



#### 회원정보수정(Update)

##### forms.py

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChanceForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', )
```

- 그냥 `UserChanceForm` 을 사용하게 되면 슈퍼계정까지 수정할 수 있기때문에 금기한다
- 따라서 `CustomUserChanceForm` 을 새로 만들어서 사용한다
- `get_user_model` 기본 유저 모델을 알 수 있다.

##### update 함수

```python
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChanceForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChanceForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)
```

### 비밀번호수정(password)

##### changepw 함수

```python
@require_http_methods(['GET', 'POST'])
def changepw(request):
    if not request.user.is_authenticated:
        return redirect('acoounts:login')
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/changepw.html', context)
```

- django에서 제공하는 `PasswordChangeForm`을 사용한다.
- 동작은 update와 크게 다르지 않지만 비밀번호 변경후 저장하게 되면 로그아웃이 되어버린다
- 따라서 `update_session_auth_hash(request, form.user)` 를 통해서 session정보를 업데이트해서 로그아웃이 풀리는 것을 막아준다.



