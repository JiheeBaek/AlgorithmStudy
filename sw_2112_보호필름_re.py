def check(A, B):
    for j in range(W):
        f=False
        cnt=1
        prev=matrix[0][j]
        if 0 in A:
            prev=0
        elif 0 in B:
            prev=1
        for i in range(1, D):
            cur=matrix[i][j]
            if i in A:
                cur=0
            elif i in B:
                cur=1
            if prev==cur:
                cnt+=1
                prev=cur
            else:
                if cnt>=K:
                    f=True
                cnt=1
                prev=cur
        if cnt>=K or f:
            continue
        else:
            return False
    return True

def ab_go(change, cur):
    global ab_vi, flag
    if cur==len(change):
        A, B=[], []
        for i in range(len(change)):
            if ab_vi[i]:
                A.append(change[i])
            else:
                B.append(change[i])
        if check(A, B):
            flag=True
        return
    ab_vi[cur]=False
    ab_go(change, cur+1)
    ab_vi[cur]=True
    ab_go(change, cur+1)

def row_go(cur, cnt):
    global ab_vi
    if cur==D:
        if cnt==ans:
            #A할지 B할지 선택
            change=[]
            for i in range(D):
                if vi[i]:
                    change.append(i)
            ab_vi=[False for _ in range(len(change))]
            ab_go(change, 0)
        return
    vi[cur]=False
    row_go(cur+1, cnt)
    vi[cur]=True
    row_go(cur+1, cnt+1)

T=int(input())
for test_case in range(1, T+1):
    D, W, K=list(map(int, input().strip().split(' ')))
    matrix=[list(map(int, input().strip().split(' '))) for _ in range(D)] #특성 A:0, B:1
    ans=0
    flag=False
    while True:
        vi=[False for _ in range(D)]
        ab_vi=[]
        row_go(0, 0)
        if flag:
            break
        ans+=1
    print('#{} {}'.format(test_case, ans))