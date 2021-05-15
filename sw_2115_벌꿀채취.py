def h_go(cur, sum):
    global small_ans
    if cur==M:
        small_h=0
        small_cost=0
        for i in range(M):
            if small_visited[i]:
                small_h+=small_matrix[i]
                small_cost+=small_matrix[i]**2
        if small_h>C:
            return
        small_ans=max(small_ans, small_cost)
        return
    small_visited[cur]=False
    h_go(cur+1, sum)
    small_visited[cur]=True
    h_go(cur+1, sum+small_matrix[cur])

def calc(x, y):
    global small_matrix, small_ans, small_visited
    h=0
    cost=0
    for c in range(y, y+M):
        h+=matrix[x][c]
        cost+=matrix[x][c]**2
    if h<=C: #최대로 담을 수 있는 꿀의 양보다 작거나 같으면 ok
        return cost
    #가격이 최대가 되도록 채취해야함
    small_matrix=matrix[x][y:y+M]
    small_ans=0
    small_visited=[False for _ in range(M)]
    h_go(0, 0)
    return small_ans

def go(flag1, flag2, x1, y1, x2, y2):
    global ans
    if flag1 and flag2:
        cost1=calc(x1, y1)
        cost2=calc(x2, y2)
        #print(x1, y1, x2, y2, cost1, cost2)
        #꿀 양 계산해서 최대가 답이 되도록
        ans=max(ans, cost1+cost2)
        return
    elif flag1 and not flag2:
        for i in range(x1, N):
            for j in range(N-M+1):
                if i==x1 and j<y1+M:
                    continue
                if not visited[i][j]:
                    visited[i][j]=True
                    go(True, True, x1, y1, i, j)
                    visited[i][j]=False

    for i in range(N): #flag1, flag2 둘 다 False
        for j in range(N-M+1):
            if not visited[i][j]:
                visited[i][j]=True
                go(True, False, i, j, x2, y2)


T=int(input())
for test_case in range(1, T+1):
    ans = 0
    N, M, C=list(map(int, input().split(' ')))
    matrix=[]
    for _ in range(N):
        matrix.append(list(map(int, input().split(' '))))
    visited = [[False for _ in range(N)] for _ in range(N)]
    small_ans = 0
    small_matrix=[]
    small_visited=[]
    go(False, False, 0, 0, 0, 0)
    print('#{} {}'.format(test_case, ans))



