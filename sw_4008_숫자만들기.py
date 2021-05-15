import math

def go(p, s, m, d, result, cur, path):
    global max_ans, min_ans
    if cur==N:
        max_ans=max(max_ans, result)
        min_ans=min(min_ans, result)
        #print(result, path)
        return
    if p>0:
        go(p-1, s, m, d, result+operand[cur], cur+1, path+'+')
    if s>0:
        go(p, s-1, m, d, result - operand[cur], cur + 1, path+'-')
    if m>0:
        go(p, s, m-1, d, result * operand[cur], cur + 1, path+'*')
    if d>0:
        go(p, s, m, d - 1, int(result / operand[cur]), cur + 1, path + '/')
T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    operator=list(map(int, input().strip().split(' ')))
    operand=list(map(int, input().strip().split(' ')))
    max_ans=-float('inf')
    min_ans=float('inf')
    go(operator[0], operator[1], operator[2], operator[3], operand[0], 1, '')
    ans=max_ans-min_ans
    print('#{} {}'.format(test_case, ans))