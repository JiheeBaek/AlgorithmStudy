def go(result, cur, p, sub, mul, div):
    global max_ans, min_ans
    if cur==N:
        max_ans=max(max_ans, result)
        min_ans=min(min_ans, result)
        return
    if p>0:
        go(result+operand[cur], cur+1, p-1, sub, mul, div)
    if sub>0:
        go(result-operand[cur], cur+1, p, sub-1, mul, div)
    if mul>0:
        go(result*operand[cur], cur+1, p, sub, mul-1, div)
    if div>0:
        go(int(result/operand[cur]), cur+1, p, sub, mul, div-1)

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    operator=list(map(int, input().strip().split(' ')))
    operand=list(map(int, input().strip().split(' ')))
    max_ans=-float('inf')
    min_ans=float('inf')
    go(operand[0], 1, operator[0], operator[1], operator[2], operator[3])
    ans=max_ans-min_ans
    print('#{} {}'.format(test_case, ans))