# Model Relationship

### fields

- 1 : N = `Foreignkey()`
- M : N = `ManyToManyField()`
- 1 : 1 = `OneToOneField()`

#### Foreignkey()

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

- Article : 참조하는 모델
- on_delete 옵션
  - `CASCADE` : 참조 된 객체가 삭제 됐을 때 참조하는 객체도 삭제
  - `PROTECT` : 참조가 되어 있는 경우 오류 발생 



#### ManyToManyField

```python
class Comment(models.Model):
    articles = models.ManyToManyField(Article, related_name='comments')
```

- related_name : 역참조시 이름설정
- through : 중간 테이블을 직접 지정하려면 through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정



#### 1:N model

- Comment(N) 이 Aritcle(1)을 참조
  - `comment.article` 
  - 모델 작성시 선언 보통
- Article(1)이 Comment(N)를 참조(역참조)
  - `article.comment_set.all()`
  - django에서 모델이름을 설정해주는데 소문자로 만들어준다
  - 모델이름_set 형식의 manager 생성



#### save method

- `save(commit=False)`
  - 객체 조작을 위해 인스턴스는 생성 하지만 저장은 X
  - 누구한테 댓글을 줄지 설정하기 위해서
  - save(commit=False) 저장하기 전단계까지 진행



### 동작순서

1. model 만들기
2. migrate
3. urls - > views 형식으로진행
4. 필요하면 form만들기



## user model

항상 첫 마이그레이션 전에 설정하기

1. 유저 모델 정의

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

2. settings.py에 AUTH_USER_MODEL 등록하기
3. makemigrations, migrate 해서 사용하기



- models 에서는` AUTH_USER_MODEL`을 통해서 사용하기
- 다른 곳에서는 `get_user_model`로 사용하기 

