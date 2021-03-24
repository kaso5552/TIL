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

