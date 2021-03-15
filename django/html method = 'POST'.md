# html method = 'POST'

1. `method = 'POST'` 로 변경
2. `{% csrf_token %}` 추가
3. 정보를 `request.POST.get()`을 통해서 추가
4. 정보를 수정, 업데이트할때만 사용 , 평소에는 'GET' 사용