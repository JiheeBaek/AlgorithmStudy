dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

def DFS(x, y, flag, h, cnt):
    global ans
    if cnt>ans:
        ans=cnt
    for d in range(4):
        nx, ny=x+dx[d], y+dy[d]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if visited[nx][ny] == True:
                continue
            if h > matrix[nx][ny]:
                visited[nx][ny] = True
                DFS(nx, ny, flag, matrix[nx][ny], cnt + 1)
                visited[nx][ny]=False
            elif flag == False and h>matrix[nx][ny]-K:
                visited[nx][ny] = True
                DFS(nx, ny, True, h-1, cnt + 1)
                visited[nx][ny] = False

T=int(input())
for test_case in range(1, T+1):
    N, K=map(int, input().split(' '))
    matrix=[]
    max=-1
    for _ in range(N):
        temp=list(map(int, input().split(' ')))
        for i in range(N):
            if temp[i]>max:
                max=temp[i]
        matrix.append(temp)

    starts=[]
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==max:
                starts.append([i, j])
    ans=1
    for s in range(len(starts)):
        x, y=starts[s]
        visited = [[False for _ in range(N)] for _ in range(N)]
        visited[x][y]=True
        DFS(x, y, False, matrix[x][y], 1)
        visited[x][y]=False

    print('#{} {}'.format(test_case, ans))