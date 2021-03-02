import sys
sys.stdin = open('sw_1224_계산기3_input.txt','r')

def Cal():
    number = []
    for i in range(len(data)):
        if data[i] == '+':
            a = number.pop()
            b = number.pop()
            number.append(a + b)
        elif data[i] == '*':
            a = number.pop()
            b = number.pop()
            number.append(a * b)
        else:
            number.append(data[i])
    return number.pop()

def Postfix():
    stack = []
    for i in range(N):
        if arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            while True:
                sample = stack.pop()
                if sample == '(':
                    break
                else:
                    data.append(sample)
        elif arr[i] == '+':
            while True:
                if len(stack) == 0 or stack[-1] == '(':
                    stack.append(arr[i])
                    break
                else:
                    data.append(stack.pop())
        elif arr[i] == '*':
            while True:
                if len(stack) == 0 or stack[-1] != '*':
                    stack.append(arr[i])
                    break
                else:
                    data.append(stack.pop())
        else:
            data.append(int(arr[i]))


T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = list(input())
    data = []
    Postfix()
    ans = Cal()
    print('#{} {}'.format(tc,ans))

