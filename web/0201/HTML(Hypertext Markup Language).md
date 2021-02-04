# HTML(Hypertext Markup Language)

웹페이지가 어떻게 구조화되어 있는지 알수있는 마크업 언어, `elements`로 구성되어있다.

[Mozilla 홈페이지](https://developer.mozilla.org/ko/) 

[HTML 기본](https://developer.mozilla.org/ko/docs/Learn/HTML/Introduction_to_HTML/Getting_started)

## Elements(요소)

여는 태그, 닫는 태그, 내용으로 구성되어 있다.

[요소 참고서](https://developer.mozilla.org/ko/docs/Web/HTML/Element)

```html
<p> <!-- opening tag -->
   	test <!-- content -->
</p> <!-- closing tag -->
```

- <!-- 주석 --> 으로 주석을 표현할 수 있다.

### Attributes(속성)

요소에 실제론 나타내고 싶지 않지만 추가적인 내용을 담을 때 사용

주의사항

	1. 하나 이상의 속성들을 적을 때는 속성사이에 공백 필수
	2. 속성 값은 `" "`로 감싸야한다.

```html
<p class="test-class" style="yellow">
    test
</p>
```

### Semantic tag(시맨틱 태그)

콘텐츠의 의미를 명확히 설명하는 태그

- 읽기 쉬워지고 접근성이 좋아지는 장점이있다.

## 문서의 기본구조

vscode에서 `!` + `enter`를 통해서 기본구조를 불러올 수 있다.

```html
<!DOCTYPE html> <!-- 문서형식을 나타낸다 -->
<html lang="en"> <!-- <html>요소로 기본요소, lang="언어"를 나타낸다 -->
<head> <!-- HTML 페이지의 주된 내용을 담고있는 요소이 -->
  <meta charset="UTF-8"> <!-- 문자인코딩 설정을 utf-8로 지정하는 요소 -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title> <!-- 페이지의 제목설정, 브라우저 탭에 표시 -->
</head>
<body> <!-- 페이지에 표시되는 모든 콘텐츠를 포함하는 요소 -->
  
</body>
</html>
```

> HTML은 공식문서를 자주 활용하자. 검색창에 "mdn 요소"를 통해서 공식홈페이지 확인 !