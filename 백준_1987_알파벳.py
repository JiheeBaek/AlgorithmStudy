#백준에서 python3로 제출 시 시간초과, pypy3로 제출 시 통과
R, C=list(map(int, input().split(' ')))
board=[]
for i in range(R):
    board.append(input())

visited=[False for _ in range(26)] #알파벳 26개
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

def DFS(x, y, cnt): #백트래킹
    global answer #python에서 global 변수는 함수 내부에서 선언해야 함
    answer=max(answer, cnt)
    for d in range(4):
        nx, ny=x+dx[d], y+dy[d]
        if 0<=nx and nx<R and 0<=ny and ny<C:
            if not visited[ord(board[nx][ny])-65]:
                visited[ord(board[nx][ny])-65]=True
                DFS(nx, ny, cnt+1)
                visited[ord(board[nx][ny])-65]=False

answer=1 #시작 위치
stack=[(0, 0, 0)]
visited[ord(board[0][0])-65]=True
ans=DFS(0, 0, 1) #x, y, cnt
print(answer)