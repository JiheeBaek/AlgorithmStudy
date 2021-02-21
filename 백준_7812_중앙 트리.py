import sys
sys.setrecursionlimit(10**6)

def getTree(here, prev):
    cnt[here]=1
    for i in range(len(vc[here])):
        next, cost = vc[here][i][0], vc[here][i][1]
        if next==prev:
            continue
        getTree(next, here)
        cnt[here]+=cnt[next]
        sum[here]+=cost*cnt[next]+sum[next]

def getSum(here, prev, total):
    global ans
    ans=min(ans, total)
    for i in range(len(vc[here])):
        next, cost = vc[here][i][0], vc[here][i][1]
        if next==prev:
            continue
        getSum(next, here, total-(cnt[next]*cost)+((N-cnt[next])*cost))


while True:
    N=int(input())
    if N==0:
        break
    vc=[[] for _ in range(N)]
    cnt = [0 for _ in range(N)]
    sum = [0 for _ in range(N)]
    ans=float('inf')

    for i in range(N-1):
        from_, to, val=list(map(int, input().split(' ')))
        vc[from_].append((to, val))
        vc[to].append((from_, val))

    getTree(0, -1)
    getSum(0, -1, sum[0])
    print(ans)