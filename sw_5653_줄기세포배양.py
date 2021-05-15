from collections import deque
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
#  상  하  좌  우
T=int(input())
for test_case in range(1, T+1):
    N, M, K=list(map(int, input().strip().split(' ')))
    matrix=[[0]*700 for _ in range(700)]
    deac = []
    ac=[]
    visited=[[False]*700 for _ in range(700)] #생길 때 visited
    queue=deque([])
    s_x, s_y=(700-N)//2, (700-M)//2
    for i in range(N):
        temp=list(map(int, input().strip().split(' ')))
        for j in range(M):
            if temp[j]!=0:
                deac.append([temp[j], s_x+i, s_y+j, 0, 0+temp[j]*2]) #생명력, x, y, 생긴 시간, 죽는 시간
                visited[s_x + i][s_y + j] = True
            matrix[s_x+i][s_y+j]=temp[j]

    for time in range(1, K+1):
        deact_ac=[]
        for i in range(len(deac)):
            if deac[i][3]+deac[i][0]==time: #활성화 되는 세포
                ac.append([deac[i][0], deac[i][1], deac[i][2], time, deac[i][4]]) #생명력, x, y, 활성화된 시간, 죽는 시간
                deact_ac.append(deac[i]) #몇번째에 있는 세포를 deac에서 지워야 하는지
        for i in range(len(deact_ac)):
            deac.remove(deact_ac[i])
        death=[]
        for i in range(len(ac)):
            if ac[i][3]+1==time: #번식하는 시간 = 활성화된 시간 + 1
                queue.append((ac[i][0], ac[i][1], ac[i][2])) #생명력, x, y
            if ac[i][4]==time: #죽는 세포
                death.append(ac[i])
        for i in range(len(death)):
            ac.remove(death[i])
        queue=deque(sorted(queue, reverse=True)) #생명력이 큰 세포 먼저 번식하도록
        while queue:
            lifetime, x, y=queue.popleft()
            for d in range(4):
                nx, ny=x+dx[d], y+dy[d]
                if 0<=nx and nx<700 and 0<=ny and ny<700:
                    if not visited[nx][ny]:
                        visited[nx][ny]=True
                        matrix[nx][ny]=lifetime
                        deac.append([lifetime, nx, ny, time, time + lifetime*2])  # 생명력, x, y, 생긴 시간, 죽는 시간
        '''
        print('\n')
        print('time:', time)
        print('deac:', deac)
        print('ac:', ac)
        print('death: ', death)
        '''
    ans=len(deac)+len(ac)
    print('#{} {}'.format(test_case, ans))





