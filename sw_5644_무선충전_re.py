from collections import deque

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def BFS(idx, s_x, s_y, c, p):
    visited=[[False]*10 for _ in range(10)]
    visited[s_x][s_y]=True
    queue=deque([(s_x, s_y, 0)])
    matrix[s_x][s_y].append(idx)
    while queue:
        x, y, cnt=queue.popleft()
        if cnt==c:
            break
        for d in range(4):
            nx, ny=x+dx[d], y+dy[d]
            if 0<=nx and nx<10 and 0<=ny and ny<10:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    matrix[nx][ny].append(idx)
                    queue.append((nx, ny, cnt+1))
    return

pdx=[0, -1, 0, 1, 0]
pdy=[0, 0, 1, 0, -1]
#이동x ,상, 우, 하, 좌

T=int(input())
for test_case in range(1, T+1):
    M, A=list(map(int, input().strip().split(' ')))
    moveA=[0]+list(map(int, input().strip().split(' ')))
    moveB=[0]+list(map(int, input().strip().split(' ')))
    matrix=[[[] for _ in range(10)] for _ in range(10)]
    BC=[]
    for i in range(A):
        y, x, c, p=list(map(int, input().strip().split(' ')))
        BFS(i, x-1, y-1, c, p)
        BC.append([x-1, y-1, c, p]) # x, y, 범위, 성능
    ax, ay=0, 0
    bx, by=9, 9
    ans=0
    for m in range(M+1):
        da, db=moveA[m], moveB[m]
        ax, ay=ax+pdx[da], ay+pdy[da]
        bx, by=bx+pdx[db], by+pdy[db]
        if len(matrix[ax][ay])==0 and len(matrix[bx][by])==0:
            continue
        elif len(matrix[ax][ay])==1 and len(matrix[bx][by])==0:
            ans+=BC[matrix[ax][ay][0]][3]
        elif len(matrix[ax][ay])==0 and len(matrix[bx][by])==1:
            ans+=BC[matrix[bx][by][0]][3]
        elif len(matrix[ax][ay])>1 and len(matrix[bx][by])==0:
            max=BC[matrix[ax][ay][0]][3]
            for i in range(1, len(matrix[ax][ay])):
                if BC[matrix[ax][ay][i]][3]>max:
                    max=BC[matrix[ax][ay][i]][3]
            ans+=max
        elif len(matrix[ax][ay])==0 and len(matrix[bx][by])>1:
            max=BC[matrix[bx][by][0]][3]
            for i in range(1, len(matrix[bx][by])):
                if BC[matrix[bx][by][i]][3]>max:
                    max=BC[matrix[bx][by][i]][3]
            ans+=max
        else:
            max=0
            a=matrix[ax][ay]
            b=matrix[bx][by]
            for i in range(len(a)):
                for j in range(len(b)):
                    if a[i]==b[j]:
                        temp=BC[a[i]][3]
                    else:
                        temp=BC[a[i]][3]+BC[b[j]][3]
                    if temp>max:
                        max=temp
            ans+=max
    print('#{} {}'.format(test_case, ans))



