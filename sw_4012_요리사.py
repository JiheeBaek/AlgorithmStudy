def calc(material):
    sum=0
    for i in range(N//2):
        for j in range(N//2):
            if i==j:
                continue
            sum+=synergy[material[i]][material[j]]
    return sum

def go(cur, cnt):
    global ans
    if cur==N:
        if cnt==N//2:
            A=[]
            B=[]
            for i in range(N):
                if visited[i]:
                    A.append(i)
                else:
                    B.append(i)
            #A음식과 B 음식에 들어갈 재료 선택 완료
            diff=abs(calc(A)-calc(B))
            ans=min(ans, diff)
        return
    visited[cur]=False
    go(cur+1, cnt)
    visited[cur]=True
    go(cur+1, cnt+1)

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    synergy=[]
    for _ in range(N):
        synergy.append(list(map(int, input().strip().split(' '))))
    ans=float('inf')
    visited=[False for _ in range(N)]
    go(0, 0)
    print('#{} {}'.format(test_case, ans))