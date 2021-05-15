from collections import deque

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

def BFS(s_x, s_y):
    queue=deque([(s_x, s_y, 1)])
    visited=[[False]*N for _ in range(N)]
    visited[s_x][s_y]=True
    if matrix[s_x][s_y]==1:
        home=1
    else:
        home=0
    while queue:
        x, y, cnt=queue.popleft()
        if cnt==K:
            break
        for d in range(4):
            nx, ny=x+dx[d], y+dy[d]
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    if matrix[nx][ny]==1:
                        home+=1
                    queue.append((nx, ny, cnt+1))
    return home

T=int(input())
for test_case in range(1, T+1):
    N, M=list(map(int, input().strip().split(' ')))
    matrix=[]
    num=0
    for i in range(N):
        temp=list(map(int, input().strip().split(' ')))
        matrix.append(temp)
        for j in range(N):
            if temp[j]==1:
                num+=1
    K=1
    ans=1
    while num*M-(K*K+(K-1)*(K-1))>=0:
        K += 1
        for i in range(N):
            for j in range(N):
                res=BFS(i, j)
                if res*M-(K*K+(K-1)*(K-1))>=0:
                    ans=max(ans, res)
    print('#{} {}'.format(test_case, ans))