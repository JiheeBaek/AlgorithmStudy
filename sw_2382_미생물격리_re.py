dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
#상:0 하:1 좌:2 우:3
def check(): #한 위치에 여러 군집이 있는지
    for i in range(N):
        for j in range(N):
            if len(matrix[i][j])<=1:
                continue
            multi=matrix[i][j]
            num=group_info[multi[0]][2]
            max=multi[0]  # 미생물 수가 제일 많은 군집의 번호
            for k in range(1, len(multi)):
                num += group_info[multi[k]][2]  # 군집에 속한 미생물 수 모두 더하기
                if group_info[multi[k]][2]>group_info[max][2]:
                    group_info[max][0], group_info[max][1]=-1, -1
                    max=multi[k]
                else:
                    group_info[multi[k]][0], group_info[multi[k]][1]=-1, -1
            group_info[max][2]=num
            matrix[i][j]=[max]
    return

def move():
    for i in range(K):
        x, y, num, dir=group_info[i]
        nx, ny=x+dx[dir], y+dy[dir]
        if 0<=nx and nx<N and 0<=ny and ny<N:
            if nx==0 or nx==N-1 or ny==0 or ny==N-1: #약품이 있는 가장자리로 이동한다면
                num=num//2 #미생물 수 절반으로 줄어들고
                #방향이 반대
                if dir==0: #상->하
                    dir=1
                elif dir==1: #하->상
                    dir=0
                elif dir==2: #좌->우
                    dir=3
                else: #우->좌
                    dir=2
            matrix[x][y].remove(i)
            if num==0: #미생물이 다 죽었으면 군집은 사라진다.
                nx, ny=-1, -1
            else:
                matrix[nx][ny].append(i)
            group_info[i]=[nx, ny, num, dir]
    return

T=int(input())
for test_case in range(1, T+1):
    N, M, K=list(map(int, input().split(' ')))
    group_info=[]
    matrix=[[[] for _ in range(N)] for _ in range(N)] #군집의 현재 위치를 나타내기 위해 각 칸에는 군집 번호 list가 있다.
    for i in range(K):
        temp=list(map(int, input().split(' '))) #x좌표, y좌표, 미생물수, 방향
        x, y=temp[0], temp[1]
        matrix[x][y].append(i) #각 군집은 0~K-1 까지 번호를 가진다
        temp[3]-=1 #방향은 0부터 시작하도록 조정
        group_info.append(temp)
    for time in range(M):
        move()
        check()
        ##########
        '''
        print(time)
        for i in range(N):
            print(matrix[i])
        for i in range(K):
            print(group_info[i])
        '''
        ##########
    ans=0
    for i in range(K):
        if group_info[i][0]==-1:
            continue
        ans+=group_info[i][2]
    print('#{} {}'.format(test_case, ans))
