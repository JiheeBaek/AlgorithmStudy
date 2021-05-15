dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
#  상  하  좌  우
#  1   2   3  4

T=int(input())
for test_case in range(1, T+1):
    N, M, K = list(map(int, input().split(' '))) #정사각형 크기, M시간 후, 군집의 수
    matrix=[[[] for _ in range(N)] for _ in range(N)]
    info=[]
    for i in range(K): #군집은 0~K번의 번호를 가지게 됨
        temp=list(map(int, input().split(' '))) #(x, y) 위치, 미생물 수, 이동방향
        matrix[temp[0]][temp[1]].append(i)
        temp[3]-=1 #dx, dy의 인덱스와 일치시키기 위함
        info.append(temp)

    for time in range(M): #time 시간 후
        for i in range(K): # i번 군집에 대한 처리
            x, y, num, d = info[i]
            if x==0 and y==0:
                continue
            nx, ny=x+dx[d], y+dy[d] #time+1에서의 위치
            #약품이 있는 곳에 위치하게 되는 경우#
            if nx==0 or nx==N-1: #이동 방향이 상/하인 경우
                if d==0: #상 -> 하
                    d=1
                elif d==1: #하 -> 상
                    d=0
                num=num//2
            elif ny==0 or ny==N-1: #이동 방향이 좌/우인 경우
                if d==2:
                    d=3
                elif d==3:
                    d=2
                num=num//2
            ###############################
            matrix[x][y].remove(i)  # 원래 자리에서 나오고
            if num>0:
                matrix[nx][ny].append(i)  # 다음 자리에 들어가고
            else: #미생물이 없으면 군집은 사라진다
                nx, ny=0, 0
            info[i]=[nx, ny, num, d]

        for i in range(N):
            for j in range(N):
                if i==0 and j==0:
                    continue
                if len(matrix[i][j])>1: #한 위치에 여러 군집이 있는 경우
                    max=matrix[i][j][0]
                    s=info[max][2]
                    l_remove=[]
                    for n in range(1, len(matrix[i][j])):
                        idx=matrix[i][j][n]
                        s += info[idx][2]
                        if info[idx][2]>info[max][2]: #더 큰 군집에 합쳐지고 max는 사라짐
                            l_remove.append(max)
                            info[max][0], info[max][1]=0, 0
                            max=idx
                        else: #다른 군집에 합쳐지고 idx는 사라짐
                            l_remove.append(idx)
                            info[idx][0], info[idx][1]=0, 0
                    info[max][2]=s
                    for r in range(len(l_remove)):
                        matrix[i][j].remove(l_remove[r])

        '''
        print(time, '시간 후')
        for i in range(K):
            print(info[i])
        print('\n')
        for i in range(N):
            print(matrix[i])
        '''
    ans=0
    for i in range(K):
        if info[i][0]==0 and info[i][1]==0:
            continue
        ans+=info[i][2]
    print('#{} {}'.format(test_case, ans))
