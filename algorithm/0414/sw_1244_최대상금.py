import sys
sys.stdin = open('sw_1244_최대상금_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    number, count = input().split()
    num_len = len(number)
    count = int(count)
    stack = [[] for _ in range(count+ 1)]
    stack[0].append(number)
    for i in range(count):
        for j in stack[i]:
            for k in range(num_len-1):
                for w in range(k+1,num_len):
                    num = list(j)
                    num[k], num[w] = num[w], num[k]
                    num = ''.join(num)
                    if num in stack[i+1]:
                        continue
                    else:
                        stack[i+1].append(num)
    print('#{} {}'.format(tc,max(stack[count])))

# 반복문으로 돌리기
    # number = list(number)
    # num_len = len(number)
    # count = int(count)
    # same_num = 10
    # for i in range(num_len-1):
    #     sample = int(number[i])
    #     change = 0
    #     if count == 0:
    #         break
    #     for j in range(i+1, num_len):
    #         change_num = int(number[j])
    #         if sample == change_num and change == 1:
    #             sample_count = j
    #             same_num = sample
    #         elif sample <= change_num :
    #             sample = change_num
    #             sample_count = j
    #             change = 1
    #     if change == 1:
    #         number[i], number[sample_count] = number[sample_count], number[i]
    #         count -= 1
    # while count > 0 :
    #     if same_num == 10:
    #         number[num_len-2], number[num_len-1] = number[num_len-1], number[num_len-2]
    #         count -= 1
    #     else:
    #         break
    # print('#{}'.format(tc),end=' ')
    # print(''.join(number))
