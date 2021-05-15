from collections import deque

dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

pdx=[0, -1, 0, 1, 0]
pdy=[0, 0, 1, 0, -1]
#  x, 상, 우, 하, 좌

def BFS(n, s_x, s_y, c):
    queue=deque([(s_x, s_y, 0)])
    while queue:
        x, y, cov=queue.popleft()
        if cov==c:
            return
        for d in range(4):
            nx, ny=x+dx[d], y+dy[d]
            if 0<=nx and nx<10 and 0<=ny and ny<10:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    matrix[nx][ny].append(n)
                    queue.append((nx, ny, cov+1))

T=int(input())
for test_case in range(1, T+1):
    M, A=list(map(int, input().strip().split(' ')))
    amove=[0]+list(map(int, input().strip().split(' ')))
    bmove=[0]+list(map(int, input().strip().split(' ')))
    bc=[] #x, y좌표, 충전 범위, 처리량
    for _ in range(A):
        temp=list(map(int, input().strip().split(' ')))
        bc.append([temp[1]-1, temp[0]-1, temp[2], temp[3]])
    matrix=[[[] for _ in range(10)] for _ in range(10)]
    for i in range(A):
        visited=[[False]*10 for _ in range(10)]
        s_x, s_y, c, p=bc[i]
        visited[s_x][s_y]=True
        matrix[s_x][s_y].append(i)
        BFS(i, s_x, s_y, c)
    ax, ay=0, 0
    bx, by=9, 9
    sum=0
    achoice, bchoice=[], []
    for t in range(M+1):
        nax, nay=ax+pdx[amove[t]], ay+pdy[amove[t]]
        nbx, nby=bx+pdx[bmove[t]], by+pdy[bmove[t]]
        if len(matrix[nax][nay])==1 and len(matrix[nbx][nby])==1:
            if matrix[nax][nay][0]==matrix[nbx][nby][0]:
                sum+=bc[matrix[nax][nay][0]][3]
            else:
                sum+=bc[matrix[nax][nay][0]][3]+bc[matrix[nbx][nby][0]][3]
        elif len(matrix[nax][nay]) > 1 and len(matrix[nbx][nby]) > 1:
            local_ans = 0
            for i in range(len(matrix[nax][nay])):
                for j in range(len(matrix[nbx][nby])):
                    if matrix[nax][nay][i] == matrix[nbx][nby][j]:
                        temp = bc[matrix[nax][nay][i]][3]
                    else:
                        temp = bc[matrix[nax][nay][i]][3] + bc[matrix[nbx][nby][j]][3]
                    local_ans = max(local_ans, temp)
            sum += local_ans
        elif len(matrix[nax][nay])>1 and len(matrix[nbx][nby])==0:
            local_ans=0
            for i in range(len(matrix[nax][nay])):
                if bc[matrix[nax][nay][i]][3]>local_ans:
                    local_ans=bc[matrix[nax][nay][i]][3]
            sum+=local_ans
        elif len(matrix[nax][nay]) > 1 and len(matrix[nbx][nby]) == 1:
            local_ans = 0
            for i in range(len(matrix[nax][nay])):
                for j in range(len(matrix[nbx][nby])):
                    if matrix[nax][nay][i] == matrix[nbx][nby][j]:
                        temp = bc[matrix[nax][nay][i]][3]
                    else:
                        temp = bc[matrix[nax][nay][i]][3] + bc[matrix[nbx][nby][j]][3]
                    local_ans = max(local_ans, temp)
            sum += local_ans
        elif len(matrix[nax][nay]) ==0 and len(matrix[nbx][nby]) > 1:
            local_ans=0
            for i in range(len(matrix[nbx][nby])):
                if bc[matrix[nbx][nby][i]][3]>local_ans:
                    local_ans=bc[matrix[nbx][nby][i]][3]
            sum+=local_ans
        elif len(matrix[nax][nay]) == 1 and len(matrix[nbx][nby]) >1:
            local_ans = 0
            for i in range(len(matrix[nax][nay])):
                for j in range(len(matrix[nbx][nby])):
                    if matrix[nax][nay][i] == matrix[nbx][nby][j]:
                        temp = bc[matrix[nax][nay][i]][3]
                    else:
                        temp = bc[matrix[nax][nay][i]][3] + bc[matrix[nbx][nby][j]][3]
                    local_ans = max(local_ans, temp)
            sum += local_ans
        elif len(matrix[nax][nay])==1 and len(matrix[nbx][nby])==0:
            sum += bc[matrix[nax][nay][0]][3]
        elif len(matrix[nax][nay]) == 0 and len(matrix[nbx][nby]) == 1:
            sum += bc[matrix[nbx][nby][0]][3]
        ax, ay=nax, nay
        bx, by=nbx, nby
        #print(t, sum, matrix[nax][nay], matrix[nbx][nby])
    #for i in range(10):
    #    print(matrix[i])

    print('#{} {}'.format(test_case, sum))