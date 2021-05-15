def h_go(list, cur, sum, cost):
    global a
    if cur==M:
        if sum<=C:
            a=max(a, cost)
        return
    #vi[cur]=False
    h_go(list, cur+1, sum, cost)
    #vi[cur]=True
    h_go(list, cur+1, sum+list[cur], cost+list[cur]**2)

def calc(h_matrix):
    global a#, vi
    h_ans=0
    for i in range(2):
        if sum(h_matrix[i])<=C:
            for j in range(M):
                h_ans+=h_matrix[i][j]**2
        else:
            #vi=[False for _ in range(M)]
            a=0
            h_go(h_matrix[i], 0, 0, 0)
            h_ans+=a
    return h_ans

def go(flag1, x1, y1, flag2, x2, y2):
    global ans
    if flag1 and flag2:
        A=matrix[x1][y1:y1+M]
        B=matrix[x2][y2:y2+M]
        small_matrix=[A, B]
        ans=max(ans, calc(small_matrix))
        return
    elif flag1 and not flag2:
        for i in range(N):
            for j in range(N-M+1):
                if i==x1 and j<y1+M:
                    continue
                go(True, x1, y1, True, i, j)
    elif not flag1:
        for i in range(N):
            for j in range(N-M+1):
                go(True, i, j, False, 0, 0)

T=int(input())
for test_case in range(1, T+1):
    N, M, C=list(map(int, input().strip().split(' ')))
    matrix=[]
    for _ in range(N):
        matrix.append(list(map(int, input().strip().split(' '))))
    a=0
    vi=[]
    ans=0
    go(False, 0, 0, False, 0, 0)
    print('#{} {}'.format(test_case, ans))