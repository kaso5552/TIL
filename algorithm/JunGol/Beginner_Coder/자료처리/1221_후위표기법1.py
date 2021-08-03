# 우리가 일반적으로 사용하는 계산방식은 중위표기법(Infix Notation)이라 하는데,
#
# A + B와 같이 피연산자 'A'와 'B' 중간에 연산자 '+'가 위치하여 이렇게 불린다.
#
# 컴퓨터공학에서는 후위표기법 (Postfix Notation)을 많이 사용하는데,
#
# 후위표기법은 A B + 와 같이 피연산자 'A'와 'B'의 뒤에 연산자 '+'가 위치한 표기법을 말한다.
#
#
#
# 중위표기법에서 (5+8)*2 와 같은 수식은 '*'가 '+'보다 연산자 우선순위가 높으므로
#
# 앞의 수식 에서처럼 5+8 을 먼저 계산해야한다면 괄호를 사용해야한다.
#
# 하지만 수식 (5+8)*2 을 후위표기법으로 바꾸면 5 8 + 2 * 와 같이 되어,
#
# 후위표기법은 괄호가 없이도 연산자의 우선 순위 를 명확히 할 수 있다는 장점이 있다.
#
# 이런 이유로 소프트웨어로 구현되는 계산기들은 후위표기 법을 많이 사용한다.
#
#
#
# 그럼 후위표기법의 수식을 입력 받아 계산하는 프로그램을 작성해 보자.
#
# 0으로 나누는 경우는 주어지지 않는다.

M = int(input())
temp = list(input().split())
number = []
for i in temp:
    if '0' <= i <= '9':
        number.append(int(i))
    else:
        num1 = number.pop(-1)
        num2 = number.pop(-1)
        if i == '+':
            number.append(num2 + num1)
        elif i == '-':
            number.append(num2 - num1)
        elif i == '*':
            number.append(num2 * num1)
        elif i == '/':
            number.append(int(num2 / num1))


print(number[0])