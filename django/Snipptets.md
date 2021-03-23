# Snipptets

자주사용하는 틀을 자동완성 시켜주는 기능이다

- vscode - file - preferences - User Snippets - New Global Snippets file을 통해서 생성가능하다.

- 기본틀

```json
{
	 "Print to console": {
	 	"scope": "javascript,typescript",
	 	"prefix": "log",
	 	"body": [
	 		"console.log("$1");",
	 		"$2"
	 	],
	 	"description": "Log output to console"
	 }
}
```

- 위와 같은 형태를 한다
  - `"Print to console"` snipptet의 이름이다
  - `"scope"` 동작할 파일 양식
  - `"prefix"` 단축기 지정
  - `"body"` 만들어 내는 틀
    - $1 , $2 등을 통해서 사용시 커서 위치를 지정할 수 있다
  - `"description"` 위의 snipptet의 설명부분이다.

