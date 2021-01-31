from collections import deque

N=int(input())
graph=[]
visit=[[False]*N for _ in range(N)]

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

for _ in range(N): #정사각형 모양의 지도
    graph.append(list(map(int, input())))

def BFS(i, j):
    count=1 #연결된 집의 개수 세기
    queue=deque([(i, j)])
    visit[i][j]=True
    while queue:
        x, y = queue.popleft()
        for n in range(4):
            nx, ny=x+dx[n], y+dy[n]
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if graph[nx][ny]==1 and visit[nx][ny]==False:
                    visit[nx][ny]=True
                    queue.append((nx, ny))
                    count+=1
    return count #하나의 단지에 속한 집의 개수


answer=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1: #집이 있으면서
            if visit[i][j]==False: #아직 counting하지 않은 위치
                n=BFS(i, j)
                answer.append(n)

print(len(answer))
answer=sorted(answer)
for i in answer:
    print(i)