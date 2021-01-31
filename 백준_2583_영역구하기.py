from collections import deque

M, N, K = list(map(int, input().split(' ')))
grid=[[0]*N for _ in range(M)] #모눈종이
for _ in range(K):
    x1, y1, x2, y2=list(map(int, input().split(' ')))
    for x in range(x1, x2): #x1, y1부터 x2, y2까지
        for y in range(y1, y2): #직사각형을 1로 표시
            grid[y][x]=1

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

def BFS(sx, sy):
    area=1 #분리된 영역의 넓이
    visited[sx][sy]=True
    queue=deque([(sx, sy)])
    while queue:
        x, y= queue.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx and nx<M and 0<=ny and ny<N:
                if grid[nx][ny]==0 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx, ny))
                    area+=1
    return area


visited=[[False]*N for _ in range(M)]
area=0
count=0
answer=[]
for i in range(M):
    for j in range(N):
        if grid[i][j]==0 and not visited[i][j]:
            area=BFS(i, j) #분리된 영역의 넓이
            answer.append(area)
            count+=1 #분리된 영역의 개수
answer=map(str, sorted(answer))

print(count)
print(' '.join(answer))

