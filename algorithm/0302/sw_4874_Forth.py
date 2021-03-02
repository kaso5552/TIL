import sys
sys.stdin = open('sw_4874_Forth_input.txt','r')


def Forth():
    for i in range(len(arr)):
        try:
            if arr[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif arr[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif arr[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif arr[i] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            elif arr[i] == '.':
                if len(stack) == 1:
                    return stack.pop()
                return 'error'
            else:
                stack.append(int(arr[i]))
        except IndexError:
            return 'error'


T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    stack = []
    ans = Forth()
    print('#{} {}'.format(tc,ans))