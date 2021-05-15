dx=[1, 1, -1, -1]
dy=[1, -1, -1, 1]

def go(x, y, prev_d): #사각형을 만들기 위한 prev_d
    global ans, i, j
    #방향은 무조건 prev_d이거나 prev_d+1이어야해
    nx, ny = x + dx[prev_d], y + dy[prev_d]
    if nx==i and ny==j and prev_d==3:
        cnt = 0
        for n in range(1, 101):  # 디저트 종류는 1~100 총 100개
            if dkind[n]:
                cnt += 1  # 디저트 개수
        ans = max(ans, cnt)
        return
    if 0 <= nx and nx < N and 0 <= ny and ny < N:  # 구역 안에 들어오는지
        if m_v[nx][ny] == False and dkind[matrix[nx][ny]] == False:  # 아직 방문하지 않은 카페이면서, 안먹은 디저트인지
            m_v[nx][ny] = True
            dkind[matrix[nx][ny]] = True
            go(nx, ny, prev_d)
            dkind[matrix[nx][ny]] = False
            m_v[nx][ny] = False


    if prev_d==3:
        return
    nx, ny = x + dx[prev_d+1], y + dy[prev_d+1]
    if nx==i and ny==j and prev_d==2:
        cnt = 0
        for n in range(1, 101):  # 디저트 종류는 1~100 총 100개
            if dkind[n]:
                cnt += 1  # 디저트 개수
        ans = max(ans, cnt)
        return
    if 0 <= nx and nx < N and 0 <= ny and ny < N:  # 구역 안에 들어오는지
        if m_v[nx][ny] == False and dkind[matrix[nx][ny]] == False:  # 아직 방문하지 않은 카페이면서, 안먹은 디저트인지
            m_v[nx][ny] = True
            dkind[matrix[nx][ny]] = True
            go(nx, ny, prev_d+1)
            dkind[matrix[nx][ny]] = False
            m_v[nx][ny] = False


T=int(input())
for test_case in range(1, T+1):
    ans=-1
    N=int(input())
    matrix=[]
    for _ in range(N):
        temp=list(map(int, input().split(' ')))
        matrix.append(temp)
    m_v=[[False]*N for _ in range(N)]
    dkind = [False for _ in range(101)]  # 디저트 종류가 100개
    dir_v=[False for _ in range(4)]
    i, j=0, 0
    for i in range(N-2):
        for j in range(1, N-1):
            m_v[i][j]=True
            dkind[matrix[i][j]]=True
            dir_v[0]=True
            go(i, j, 0)
            dir_v[0]=False
            dkind[matrix[i][j]]=False
            m_v[i][j]=False
    print('#{} {}'.format(test_case, ans))


