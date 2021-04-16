import sys
sys.stdin = open('sw_4366_은행업무_input.txt', 'r')

def cal2():
    for i in range(len(num2)):
        c_sample = c_num2
        if num2[i] == '0':
            c_sample += (2 ** (len(num2)-1-i))
        else:
            c_sample -= (2 ** (len(num2)-1-i))

        num2_list.append(c_sample)

def cal3():
    for i in range(len(num3)):
        c_sample1 = c_num3
        c_sample2 = c_num3
        if num3[i] == '0':
            c_sample1 += (3 ** (len(num3)-1-i))
            if c_sample1 in num2_list:
                return c_sample1
            c_sample2 += 2 * (3 ** (len(num3)-1-i))
            if c_sample2 in num2_list:
                return c_sample2
        elif num3[i] == '1':
            c_sample1 -= (3 ** (len(num3) - 1 - i))
            if c_sample1 in num2_list:
                return c_sample1
            c_sample2 += (3 ** (len(num3) - 1 - i))
            if c_sample2 in num2_list:
                return c_sample2
        else:
            c_sample1 -= 2 * (3 ** (len(num3) - 1 - i))
            if c_sample1 in num2_list:
                return c_sample1
            c_sample2 -= (3 ** (len(num3) - 1 - i))
            if c_sample2 in num2_list:
                return c_sample2


T = int(input())
for tc in range(1,T+1):
    num2 = input()
    num3 = input()
    c_num2 = 0
    count = 0
    for j in range(len(num2) - 1, -1, -1):
        c_num2 += int(num2[j]) * (2 ** count)
        count += 1

    c_num3 = 0
    for j in range(len(num3) - 1, -1, -1):
        if num3[j] == '1':
            c_num3 += (3 ** (len(num3)- 1 - j))
        elif num3[j] == '2':
            c_num3 += 2 * (3 ** (len(num3)- 1 - j))

    num2_list = []
    cal2()
    ans = cal3()
    print('#{} {}'.format(tc, ans))
