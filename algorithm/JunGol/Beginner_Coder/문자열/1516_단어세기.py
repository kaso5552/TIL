# 임의의 문장을 입력받아 각 단어별로 나눈 후에 단어들의 중복되는 개수를 구하는 프로그램을 작성하시오.
#
#
#
# <처리조건>
#
# (1) 입력된 스트링은 글자의 제한은 없다. 즉, 알파벳 대.소문자, 공백, ', ' 등도 입력으로 들어 올 수 있다.
#
# (2) 입력된 문장에서 각 단어사이의 구분은 공백으로 한다.
#
# (3) 단어에는 공백을 제외한 모든 문자들이 포함된다.​

# <입력형식>
# 임의의 문장을 입력받는다.(문장의 길이는 200 이하)
#
# 하나의 결과가 나온 후에도 계속 새로운 입력을 받다가, "END"가 입력되면 프로그램을 종료한다. (문장의 개수를 30을 넘지 않는다.)

while True:
    arr = list(input().split()) # I AM DOG DOG DOG DOG A AM I
    if arr[0] == 'END':
        break
    ans = {}
    temp = []
    for i in arr:
        if i in temp :
            ans[i] += 1
        else:
            ans[i] = 1
            temp.append(i)
    # 정렬하면 tuple형태로 변경
    # sorted(ans.items(), key=(lanbda x:x[1]), reverse = True) -< value기준 정렬
    ans = sorted(ans.items())# [('A', 1), ('AM', 2), ('DOG', 4), ('I', 2)]
    for key,value in ans:
        print(f'{key} : {value}')