# 양의 정수를 입력받아 역으로 보여주고 각 자리 숫자의 합을 구하는 프로그램을 작성하라.

# num_check = 1
# while num_check != 0:
#     num =

while True:
    num = int(input())
    if int(num) == 0:
        break
    ans = 0
    ans_sum = 0
    while num != 0 :
        ans = ans * 10 + num % 10
        ans_sum += num % 10
        num = int(num / 10)
    print(ans, ans_sum)

