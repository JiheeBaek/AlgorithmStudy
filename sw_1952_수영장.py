def DFS(total, left, cnt): #cnt 달까지의 금액, 3개월권 때문에 사용하는 left, 몇번째 달인지 cnt
    global ans
    if cnt==12:
        ans=min(ans, total)
        return
    if left>0: #3개월권인 경우
        DFS(total, left-1, cnt+1)
        return

    DFS(total+plan[cnt]*cost[0], 0, cnt+1) #1일권
    DFS(total+cost[1], 0, cnt+1) #한달권
    DFS(total+cost[2], 2, cnt+1) #3개월권
    DFS(cost[3], 0, 12) #1년


T=int(input())
for test_case in range(1, T+1):
    cost=list(map(int, input().split(' ')))
    plan=list(map(int, input().split(' ')))
    ans=float('inf')
    DFS(0, 0, 0)
    print('#{} {}'.format(test_case, ans))