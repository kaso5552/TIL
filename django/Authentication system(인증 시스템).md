# Authentication system(인증 시스템)

기본적인 built-in form 제공 

- `UserCreationForm`(회원가입)
- `AuthenticationForm`(로그인)

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



#### 회원탈퇴(Delete)

##### delete함수

```python
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
```







