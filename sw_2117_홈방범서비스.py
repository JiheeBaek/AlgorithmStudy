from collections import deque

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

def BFS(s_x, s_y):
    queue=deque([(s_x, s_y, 1)]) #x, y좌표, 몇번째 퍼뜨렸는지 = K
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
                    queue.append((nx, ny, cnt+1))
                    if matrix[nx][ny]==1:
                        home+=1
    return home

T=int(input())
for test_case in range(1, T+1):
    N, M =list(map(int, input().split(' ')))
    matrix=[]
    t_home=0
    for _ in range(N):
        temp=list(map(int, input().split(' ')))
        matrix.append(temp)
        for i in range(N):
            if temp[i]==1:
                t_home+=1
    ans=1
    num=1
    K=2
    #while num!=t_home: #N*N의 구역에 있는 모든 집을 커버할 수 있는 K 값이 되면 STOP - 이건 실패
    while t_home*M-(K*K+(K-1)*(K-1))>=0: #전체 집이 낼 수 있는 비용과 서비스 비용 비교 - 이건 패스 !!!여기가 중요!!!
        for i in range(N):
            for j in range(N):
                num = BFS(i, j)
                if num*M-(K*K+(K-1)*(K-1))>=0:
                    ans=max(ans, num)
        K += 1
    print('#{} {}'.format(test_case, ans))