def calc(A, B):
    asyn, bsyn=0, 0
    for i in range(N//2):
        for j in range(N//2):
            asyn+=matrix[A[i]][A[j]]
            bsyn+=matrix[B[i]][B[j]]
    return asyn, bsyn

def go(cur, cnt):
    global ans
    if cur==N:
        if cnt==N//2:
            A, B=[], []
            for i in range(N):
                if check[i]:
                    A.append(i)
                else:
                    B.append(i)
            asyn, bsyn=calc(A, B)
            ans=min(ans, abs(asyn-bsyn))
        return
    check[cur]=False
    go(cur+1, cnt)
    check[cur]=True
    go(cur+1, cnt+1)

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    matrix=[list(map(int, input().strip().split(' '))) for _ in range(N)]
    ans=float('inf')
    check=[False for _ in range(N)]
    go(0, 0)
    print('#{} {}'.format(test_case, ans))