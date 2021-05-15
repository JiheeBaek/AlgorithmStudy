from collections import deque

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
#   상, 하, 좌, 우

def BFS(s_x, s_y):
    queue=deque([(s_x, s_y, 1)])
    visited = [[False] * M for _ in range(N)]
    visited[s_x][s_y]=True
    cnt=1
    while queue:
        x, y, t=queue.popleft()
        if t==L:
            break
        for d in range(4):
            if matrix[x][y][d]:
                nx, ny=x+dx[d], y+dy[d]
                if d==0:
                    nd=1
                elif d==1:
                    nd=0
                elif d==2:
                    nd=3
                else:
                    nd=2
                if 0<=nx and nx<N and 0<=ny and ny<M:
                    if not matrix[nx][ny][nd]:
                        continue
                    if not visited[nx][ny]:
                        visited[nx][ny]=True
                        queue.append((nx, ny, t+1))
                        cnt+=1
        '''
        print(t)
        for i in range(N):
            print(visited[i])
        '''
    return cnt


T=int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = list(map(int, input().split(' ')))
    matrix=[[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]

    for i in range(N):
        temp=list(map(int, input().split(' ')))
        for j in range(M):
            if temp[j]==0:
                continue
            elif temp[j]==1: #상하좌우
                matrix[i][j]=[True, True, True, True]
            elif temp[j]==2: #상하
                matrix[i][j]=[True, True, False, False]
            elif temp[j]==3: #좌우
                matrix[i][j]=[False, False, True, True]
            elif temp[j]==4: #상우
                matrix[i][j]=[True, False, False, True]
            elif temp[j]==5: #하우
                matrix[i][j]=[False, True, False, True]
            elif temp[j]==6: #하좌
                matrix[i][j]=[False, True, True, False]
            elif temp[j]==7: #상좌
                matrix[i][j]=[True, False, True, False]

    ans=BFS(R, C)
    print('#{} {}'.format(test_case, ans))


