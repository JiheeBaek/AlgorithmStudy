import sys
sys.setrecursionlimit(10**6)

N, M=list(map(int, input().split(' '))) #전체 노드 개수 N, 트리의 에지 개수 N-1, 전체 에지 개수 M, 백에지 개수 M-(N-1)
adj=[[] for _ in range(N+1)] #인접 노드 정보 i번 인덱스에는 i번 노드와 인접한 노드 리스트가 들어있다.
for i in range(M):
    a, b=list(map(int, input().split(' ')))
    adj[a].append(b)
    adj[b].append(a) #양방향 그래프이기 때문에 각각 두개 노드 기준으로 입력 정보 저장

check=[0 for _ in range(N+1)] #노드 방문 순서 기록, i번 노드를 몇번째로 방문하는지 정보
child=[[] for _ in range(N+1)] #자식 노드 정보, i번 인덱스에는 i번 노드의 자식 노드 리스트가 들어있다.
pe=[0 for _ in range(N+1)] #parent edge: 부모랑 연결되는 간선 "트리의 에지 개수 N-1"에 포함되는 간선
we=[0 for _ in range(N+1)] #weak edge  개수 정보        이 둘의 차이점을 잘 모르겠음!!!!!!!!!!!!!!
se=[0 for _ in range(N+1)] #strong edge   개수 정보

def dfs(u, p): #vertex와 parent
    for i in range(len(adj[v])):
        w=adj[u][i] #v번 노드와 연결된 노드
        if p==w: #자기 자신은 제외
            continue
        if check[w]==0: #w번 노드를 아직 방문하지 않은 경우
            check[w]=check[v]+1 #w번 노드는 v번 노드를 방문한 뒤에 방문하기 때문에 v번 노드 방문 순서 +1
            child[u].append(w) #w가 v의 자식노드임을 알게됨

            temp=se[v]
            dfs(w, u) #w와 그 부모 노드인 v
            pe[w]=se[u]-temp

            se[u]+=se[w] #자식 노드의 백에지는 부모 노드의 백에지에 포함된다.
            we[u]+=we[w]

        elif check[u]>check[w]: #v가 부모, w가 자식이라고 생각했을 때, v를 더 늦게 방문했다는 것은 백에지가 존재한다는 의미
            we[u]+=1 #v를 부모로하는 백에지
            se[w]+=1 #w에서 나가는 백에지

check[1]=1 #1번 노드를 시작점으로 트리구조를 파악
dfs(1, 0)
ans=0

'''
1) i를 루트로 하는 서브 스패닝 트리에서 그 자식을 루트로 하는 서브 스패닝 트리에 백에지가 존재하면 불가능
   여기서의 백에지는 서브 스패닝 트리 내에서만의 백에지
2) i를 루트로 하는 서브 스패닝 트리에서, 그 자식을 루트로 하는 서브 스패닝 트리에서 i의 조상으로 2개 이상의 백에지가 있다면 불가능
3) 1)과 2)를 제외한 후에도 백에지가 존재한다면 불가능
'''

for i in range(1, N+1):
    flag=False #백에지가 있으면 True, 없으면 False
    for j in range(len(child[i])):
        v=child[i][j]
        if se[v] or we[v]-pe[v]>1: # 1)과 2) 확인
            flag=True
            break
    if flag or (M-(N-1))-we[i]!=0: # 3)확인
        continue
    ans+=i #백에지가 존재하지 않는 노드는 가능

print(ans)
