def go(cur, cost, left):
    global ans
    if cur==12:
        ans=min(ans, cost)
        return
    if left>0:
        go(cur+1, cost, left-1)
        return
    go(cur+1, cost+plan[cur]*cost_info[0], 0) #1일권
    go(cur+1, cost+cost_info[1], 0) #1달권
    go(cur+1, cost+cost_info[2], 2) #3달권
    go(12, cost_info[3], 0) #1년권

T=int(input())
for test_case in range(1, T+1):
    cost_info=list(map(int, input().split(' '))) #1일, 1달, 3달, 1년
    plan=list(map(int, input().split(' '))) #1년간 이용 계획
    ans=float('inf')
    go(0, 0, 0)
    print('#{} {}'.format(test_case, ans))