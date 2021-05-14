# git branch

가지를 통해서 본인이 수정한 부분을 정확히 알 수 있고 협업시에 한곳으로 합칠 수 있다.

- 가지 만들기 : `git branch feature/singup`
- 가지로 이동하기 : `git switch feature/signup`
- 파일 수정후 커밋 

- 커밋 이후에
  - 하나로 합치는 과정을 어떻게 할건지 결정 ( 웹 or 로컬)\
  - 마스터로 돌아와서 : `git switch master`
  - 가지를 합치고 : `git merge feature/signup`
- push 하기

- 다른사람이 pull을 한 이후 :  `git pull origin master`
  - 문제 발생, 가지랑 마스터랑 충돌이 일어남( 선택해야함 3가지 조건 중에 합칠지 없앨지 원래있던대로 남길지)
- `git merge`를 통해서 합치기
- 반복



#### 연속 커밋

1. 브렌치(dec) 만들기
2. 커밋남기기
3. 또 브렌치(a) 만들기
4. 커밋 남기기
5. 처음 가지(dec)로 돌아가기
6. `git merge` 로 합치기



1. 서로 branch에서 작업하기  
   - git branch 이름
   - git switch 이름 
2. 작업후 push 하기 (다른사람이 merge확인하기) -> 합치기  
   - 본인이 push하기전에 다른사람이 push 했을경우
   - git switch master로 이동 -> git pull origin master (최신상태 유지) -> 다시 브렌치로 이동해서 push 하기