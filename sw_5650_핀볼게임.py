dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
#   위  오  아  왼

def game_start(s_x, s_y, dir):
    x, y=s_x, s_y
    cnt=0
    while True:
        print(x, y)
        x, y=x+dx[dir], y+dy[dir]
        if x==s_x and y==s_y:
            break
        if matrix[x][y]==-1:
            break
        elif matrix[x][y]==0:
                dir=dir
        elif matrix[x][y]==1:
            cnt += 1
            if dir==0:
                dir=2
            elif dir==1:
                dir=3
            elif dir==2:
                dir=1
            else:
                dir=0
        elif matrix[x][y]==2:
            cnt += 1
            if dir==0:
                dir=1
            elif dir==1:
                dir=3
            elif dir==2:
                dir=0
            else:
                dir=2
        elif matrix[x][y]==3:
            cnt += 1
            if dir==0:
                dir=3
            elif dir==1:
                dir=2
            elif dir==2:
                dir=0
            else:
                dir=1
        elif matrix[x][y]==4:
            cnt += 1
            if dir==0:
                dir=2
            elif dir==1:
                dir=0
            elif dir==2:
                dir=3
            else:
                dir=1
        elif matrix[x][y]==5:
            cnt += 1
            if dir==0:
                dir=2
            elif dir==1:
                dir=3
            elif dir==2:
                dir=0
            else:
                dir=1
        elif 6<=matrix[x][y] and matrix[x][y]<=10:
            num=matrix[x][y]
            if (x, y)==worm[num-6][0]:
                x, y=worm[num-6][1]
            else:
                x, y=worm[num-6][0]
    return cnt

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    matrix=[[5 for _ in range(N+2)]]
    worm=[[] for _ in range(5)]
    starts=[]
    for i in range(N):
        temp=list(map(int, input().strip().split(' ')))
        matrix.append([5]+temp+[5])
        for j in range(N):
            if temp[j]==0:
                starts.append([i, j])
            elif 6<=temp[j] and temp[j]<=10:
                worm[temp[j]-6].append((i, j))
    matrix.append([5 for _ in range(N+2)])
    ans=0
    for i in range(len(starts)):
        x, y=starts[i][0], starts[i][1]
        for d in range(4):
            result=game_start(x, y, d)
            ans=max(ans, result)
    print('#{} {}'.format(test_case, ans))