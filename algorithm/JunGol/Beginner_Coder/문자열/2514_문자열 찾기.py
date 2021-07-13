# 주어진 문자열에서 연속 3개의 문자가 IOI 이거나 KOI인 문자열이 각각 몇 개 있는지 찾는 프로그램을 작성하라.

# 문자열은 알파벳의 대문자로만 이루어진다.
#
# 예를 들어 "KOIOIOI"라는 문자열은 KOI 1개 , IOI 2개가 포함되어있다.

arr = list(input())
ansK = 0
ansI = 0
for i in range(len(arr)-2):
    if arr[i] == 'K' and arr[i+1] == 'O' and arr[i+2] == 'I':
        ansK += 1
    elif arr[i] == 'I' and arr[i+1] == 'O' and arr[i+2] == 'I':
        ansI += 1

print(f'{ansK}\n{ansI}')