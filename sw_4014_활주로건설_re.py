def check(li):
    pre=li[0]
    cnt=1
    for i in range(1, N):
        if li[i]==pre:
            cnt+=1
        elif li[i]-pre==1: #_-
            if cnt>=X:
                cnt=1
            else:
                return 0
        elif li[i]-pre==-1: #-_
            if i+X>N:
                return 0
            if [li[i] for _ in range(X)]==li[i:i+X]:
                cnt=1-X
            else:
                return 0
        else:
            return 0
        pre=li[i]
    return 1

T=int(input())
for test_case in range(1, T+1):
    N, X=list(map(int, input().strip().split(' ')))
    matrix=[list(map(int, input().strip().split(' '))) for _ in range(N)]
    ans=0
    #행에 대하여
    for i in range(N):
        ans+=check(matrix[i])
        #print(ans, matrix[i])
    #열에 대하여
    for j in range(N):
        col = []
        for i in range(N):
            col.append(matrix[i][j])
        ans+=check(col)
        #print(ans, col)
    print('#{} {}'.format(test_case, ans))