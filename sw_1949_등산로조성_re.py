dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

def DFS(x, y, flag, cnt, h):
    global ans
    if cnt>ans:
        ans=cnt
    for d in range(4):
        nx, ny=x+dx[d], y+dy[d]
        if 0<=nx and nx<N and 0<=ny and ny<N:
            if visited[nx][ny]:
                continue
            if h>matrix[nx][ny]:
                visited[nx][ny]=True
                DFS(nx, ny, flag, cnt+1, matrix[nx][ny])
                visited[nx][ny]=False
            elif not flag and matrix[nx][ny]-K<matrix[x][y]:
                visited[nx][ny]=True
                DFS(nx, ny, True, cnt+1, matrix[x][y]-1)
                visited[nx][ny]=False

T=int(input())
for test_case in range(1, T+1):
    N, K=list(map(int, input().split(' ')))
    matrix=[]
    max=0
    for i in range(N):
        temp=list(map(int, input().split(' ')))
        for j in range(N):
            if temp[j]>max:
                max=temp[j]
        matrix.append(temp)
    starts=[]
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==max:
                starts.append([i, j])
    ans = 1
    for i in range(len(starts)):
        visited=[[False for _ in range(N)] for _ in range(N)]
        s_x, s_y=starts[i]
        visited[s_x][s_y]=True
        DFS(s_x, s_y, False, 1, matrix[s_x][s_y]) #현재 좌표, 깎았는지 여부, 등산로 길이, 현재 위치의 높이
        visited[s_x][s_y]=False
    print('#{} {}'.format(test_case, ans))