# image kit

[image kit](https://pypi.org/project/django-imagekit/)

이미지를 처리하기 위한 django app 이다

### 사용순서

1. `pip install django-imagekit`
2. `settings`의 `INSTALLED_APPS`에 `imagekit`추가하기
3. `models.py`에서

```python
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
```

- 위에 import하고 사용하기

- `avatar_thumbnail`은 db에 표시되지 않는다
- ImageField
  - upload_to 저장위치를 설정
- ImageSpecField
  - source 기본크기를 어떤거에 대해서 수행할것이냐
  - processors=[ResizeToFill(100, 50)] 크기 설정
  - format='JPEG' 저장되는 파일형식
  - options={'quality': 60} 압축률

3. -1 

```python
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    avatar_thumbnail = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 60})
```

- db로 설정한다

 