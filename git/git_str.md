## Github 관리

### Git 개념

	git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다

### Git 설정

 - 전역 영역에서 commit 기록의 주인을 등록

   ```
   $ git config --global user.name "username"
   $ git config --global user.email "edu@hphk.kr"
   ```

### Git 기본

	- git init 해당 디렉토리를 Git이 관리하도록 초기화
	- add 파일명 커밋할 목록에 추가
	- commit -m "커밋 메시지" (히스토리의 한 단위) 만들기
	- git push origin master 현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋 반영

### Git 저장소

| 로컬(working directory) | staging area | remote                                      | repository(github, bitbucket, gitlab) |
| :---------------------- | ------------ | ------------------------------------------- | ------------------------------------- |
|                         |              | 로컬 컴퓨터 저장소 해당 버전의 스냅샷(기록) | 원격 저장소                           |

### Git branch

	- 같은 작업물을 기반으로 동시에 다양한 작업을 할 수 있게 만들어 주는 기능
	- 독립적인 작업 영역 안에서 마음대로 소스코드를 변경할 수 있다. 분리된 작업 영역에서 변경된 내용은 추후에 기존 버전과 비교해서 새로운 하나의 버전을 만들어 낼 수 있다.

### 기본적인 등록순서

```
git init
git add README.md
git commit -m "first commit"
git branch -M main(생략)
git remote add origin https://github.com/kaso5552/TIL.git
git push -u origin master
```

### 기본적인 명령어

* `ls` : 현재 있는 곳의 내용을 나타낸다
* `cd` '경로' : '경로'로 이동한다 , `..`  상위폴더로 이동한다  
* `mkdir` '폴더명' : 폴더를 생성한다
* `touch` '파일명' : 파일을 생성한다
* `code .`  : 현재 폴더에서 VScode를 연다
* `git init`  :현재폴더부터 git으로 관리한다.
* `git config --global user.email`  '이메일'  : 이메일 등록함 (최초 1번만)
* `git config --global user.name` '이름'  : 이름을 등록함 (최초 1번만)
* `git status`  :상태가 출력된다
* `git add .`  : 이 폴더밑으로 다 git에 추가함
* `shift insert`  : 복사한 파일 붙여넣기
* `git remote -v` : remote 정보를 확인한다

#### 느낀점

	- sw개발자로써 첫시작을 한 것 같다. 아직 github에 익숙해 지려면 연습을 많이해야겠다. 우선은 평일만이라도 잔디를 꽉꽉 채워보자