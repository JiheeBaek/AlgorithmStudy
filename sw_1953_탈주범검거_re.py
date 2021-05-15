from collections import deque

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
#  상  하  좌  우

def BFS():
    cnt=1
    queue = deque([(R, C, 1)])
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    while queue:
        x, y, time=queue.popleft()
        if time==L:
            break
        direction=matrix[x][y]
        for d in range(len(direction)):
            nx, ny=x+dx[direction[d]], y+dy[direction[d]]
            if 0<=nx and nx<N and 0<=ny and ny<M:
                if not visited[nx][ny]:
                    if direction[d]==0:
                        next=1
                    elif direction[d]==1:
                        next=0
                    elif direction[d]==2:
                        next=3
                    else:
                        next=2
                    if next in matrix[nx][ny]:
                        cnt+=1
                        visited[nx][ny]=True
                        queue.append((nx, ny, time+1))
    #for i in range(N):
    #    print(visited[i])
    return cnt

T=int(input())
for test_case in range(1, T+1):
    N, M, R, C, L=list(map(int, input().split(' ')))
    matrix=[[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        temp=list(map(int, input().split(' ')))
        for j in range(M):
            if temp[j]==0:
                dir=[]
            elif temp[j]==1: #상하좌우
                dir=[0, 1, 2, 3]
            elif temp[j]==2: #상하
                dir=[0, 1]
            elif temp[j]==3: #좌우
                dir=[2, 3]
            elif temp[j]==4: #상우
                dir=[0, 3]
            elif temp[j]==5: #하우
                dir=[1, 3]
            elif temp[j]==6: #하좌
                dir=[1, 2]
            else: #상좌
                dir=[0, 2]
            matrix[i][j]=dir
    ans=BFS()
    print('#{} {}'.format(test_case, ans))