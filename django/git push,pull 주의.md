# git push,pull 주의

- `pip freeze` : 다운로드 된 pip 버전을 보여준다
  - `> requirments.txt` pip freeze파일을 > 뒤에 넣어주세요 . (리눅스 명령어)

- `pip install -r requirements.txt`  requirements에서 불러온 버전 파일들을 설치한다.

`python manage.py dumpdata --indent 4 movies.movie` 더미데이터를 출력해줌 json느낌으로

`python manage.py loaddata movies/movies.json`  db데이타에 저장됨

