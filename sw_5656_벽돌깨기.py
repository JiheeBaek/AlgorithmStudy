from copy import deepcopy

def counting():
    global loc_matrix
    cnt=0
    for i in range(H):
        for j in range(W):
            if loc_matrix[i][j]!=0:
                cnt+=1
    return cnt

def drop():
    global loc_matrix
    for j in range(W):
        first=False
        for i in range(H-1, -1, -1):
            if loc_matrix[i][j]==0 and not first:
                first=True
                loc=i
            elif loc_matrix[i][j]!=0 and first:
                loc_matrix[loc][j]=loc_matrix[i][j]
                loc_matrix[i][j]=0
                loc-=1
            else:
                continue

def breaking(x, y):
    global loc_matrix
    if 0>x or x>=H or 0>y or y>=W:
        return
    if loc_matrix[x][y]==0:
        return
    if loc_matrix[x][y]==1:
        loc_matrix[x][y]=0
        return
    power=loc_matrix[x][y]-1
    loc_matrix[x][y]=0
    for i in range(x-power, x+power+1):
        breaking(i, y)
    for i in range(y-power, y+power+1):
        breaking(x, i)

def find_top(col):
    global loc_matrix
    for i in range(H):
        if loc_matrix[i][col]!=0:
            return i
    return -1

def go(cnt, seq):
    global ans, loc_matrix
    if cnt==N:
        loc_matrix=deepcopy(matrix)
        for n in range(N):
            row=find_top(seq[n])
            breaking(row, seq[n])
            drop()
        ans=min(ans, counting())
        return
    for i in range(W):
        seq.append(i)
        go(cnt+1, seq)
        seq.pop()

T=int(input())
for test_case in range(1, T+1):
    N, W, H=list(map(int, input().strip().split(' '))) #구슬 개수, 가로, 세로
    matrix=[list(map(int, input().strip().split(' '))) for _ in range(H)]
    loc_matrix=[]
    ans=float('inf')
    go(0, []) #W개의 위치 중 중복 순열로 어느 위치에서 구슬을 떨어뜨릴지 결정
    print('#{} {}'.format(test_case, ans))