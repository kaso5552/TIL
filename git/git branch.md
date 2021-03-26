git branch feature/singup

git switch feature/signup

그다음 수정

그다음 깃 커밋



하나로 합치는 과정을 어떻게 할건지 결정 ( 웹 or 로컬)

git switch master

git merge feature/signup( 마스터랑 가지랑 합치기 )

git push origin master ( 올리기 )



그다음 b 는 마스터상태에서 땡기기

git pull origin master

- 문제 발생, 가지랑 마스터랑 충돌이 일어남( 선택해야함 3가지 조건 중에 합칠지 없앨지 원래있더넉 남길지)

그다음 git merge를 통해서 합치기

브렌치(dec) - 만들고 커밋남기기 그다음 - 또 브렌치(a) - 깃 커밋 - dec으로 돌아가기 그다음  git merge featur/a

