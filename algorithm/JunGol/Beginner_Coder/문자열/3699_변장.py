# 정올이는 스파이 이다.
#
# 변장술의 달인으로 이전과 같은 조합의 의상을 입고 밖을 나가지 않는다.
#
# 어제 안경, 코트, 신발을 입었다면 오늘은 안경대신에 썬그라스를 쓰거나
#
# 바지를 추가로 입거나 한다.
#
#
#
# 정올이가 가진 의상(장신구포함)​에 대한 정보를 입력받아
#
# 정올이가 적어도 하나 이상의 의상(장신구포함)​을 갖춘 상태로
#
# 밖을 나갈 수 있는 날은 며칠이나 될까?
#
#
#
# 예를 들어 3개의 의상이 아래와 같이 주어졌다고 하자.
#
#
#
# hat headgear
#
# sunglasses eyewear
#
# turban headgear​
#
#
#
# 이 경우 ​headgear​에 해당하는 의상이 hat, turban이고
#
# eyewear​에 해당하는 의상이 sunglasses​ 이므로 다음 5가지 조합이 가능하다.
#
# (hat), (turban), (sunglasses), (hat, sunglasses), (turban, sunglasses)

# <input>
# 첫 행에 테스트 케이스 TC( 1 <= TC <= 100)가 입력된다.
#
# 각 테스트 케이스의 첫 행에는 정올이가 가진 의상의 수 N( 0 <= N <= 30)이 입력된다.
#
# 다음 N개의 행에 의상 이름과 의상 분류 이름이 각각 문자열로 주어진다.
#
# 각 문자열의 길이는 1 ~ 20 이다. 의상 이름은 유일하다.

# <output>
# 각 테스트 케이스에 대하여 정올이가 밖에 나갈 수 있는 최대일수를 출력한다.

TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = list([input().split() for _ in range(N)])
    ans = {}
    temp = []
    result = 1
    for name,kind  in arr:
        if kind in temp:
            ans[kind].append(name)
        else:
            temp.append(kind)
            ans[kind] = [name]
    for i in ans.values():
        result *= (len(i)+1)
    print(result-1)