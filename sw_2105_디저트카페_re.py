dx=[1, 1, -1, -1]
dy=[1, -1, -1, 1]

def DFS(x, y, prev_d):
    global ans
    for d in range(2):
        if prev_d+d==4:
            return
        nx, ny=x+dx[prev_d+d], y+dy[prev_d+d]
        if 0<=nx and nx<N and 0<=ny and ny<N:
            if nx==i and ny==j and (prev_d+d)==3:
                cnt=0
                for r in range(101):
                    if eat[r]:
                        cnt+=1
                ans=max(ans, cnt)
                return
            if not visited[nx][ny] and not eat[matrix[nx][ny]]:
                visited[nx][ny]=True
                eat[matrix[nx][ny]]=True
                DFS(nx, ny, prev_d+d)
                eat[matrix[nx][ny]]=False
                visited[nx][ny]=False

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    matrix=[list(map(int, input().strip().split(' '))) for _ in range(N)]
    ans=-1
    i, j=0, 0
    for i in range(N-2):
        for j in range(1, N-1):
            visited=[[False]*N for _ in range(N)]
            eat=[False for _ in range(101)] #1~100번 디저트
            visited[i][j]=True
            eat[matrix[i][j]]=True
            DFS(i, j, 0)
            eat[matrix[i][j]]=False
            visited[i][j]=False
    print('#{} {}'.format(test_case, ans))
