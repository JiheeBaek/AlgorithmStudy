def calc(s_list, s_len):
    if len(s_list)==0: #이 계단으로 온 사람이 0명일 때
        return 0
    if len(s_list)<=3: #계단 위에는 최대 3명까지 올라갈 수 있음
        return s_list[-1]+1+s_len
    #이 계단에 4명 이상 오는 경우
    on_stair=[s_list[2], s_list[1], s_list[0]]
    s_list=s_list[3:]
    while s_list:
        next=s_list[0]
        if on_stair[-1]+1+s_len <= next+1:
            on_stair.pop()
            on_stair=[next]+on_stair
            s_list=s_list[1:]
        else: #기다려야한다면
            s_list[0]=on_stair[-1]+1+s_len -1
    return on_stair[0]+1+s_len

def go(cur):
    global ans
    if cur==num:
        s1_list=[] #사람이 몇 분에 도착하는지에 대한 정보
        s2_list=[]
        for i in range(num):
            if visited[i]: #1번 계단 입구
                s1_list.append(people[i][0])
            else: #2번 계단 입구
                s2_list.append(people[i][1])
        s1_list=sorted(s1_list) #계단 입구에 도착하는 순서대로 정렬
        s2_list=sorted(s2_list)
        t=max(calc(s1_list, s1_len), calc(s2_list, s2_len))
        ans=min(ans, t)
        return

    visited[cur]=False
    go(cur+1)
    visited[cur]=True
    go(cur+1)

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    matrix=[]
    people=[] #사람의 위치 x, y
    stairs=[] #계단의 위치 x, y  길이는 이따가 구할 것
    for i in range(N):
        temp=list(map(int, input().split(' ')))
        matrix.append(temp)
        for j in range(N):
            if temp[j]==0: #계단이면
                continue
            elif temp[j]==1: #사람이면
                people.append([i, j])
            else: #계단이면
                stairs.append([i, j])
    num=len(people) #사람 수
    s1_len=matrix[stairs[0][0]][stairs[0][1]]
    s2_len=matrix[stairs[1][0]][stairs[1][1]]
    for i in range(num):
        #1번 계단 입구에 도착하는 시간, 2번 계단 입구에 도착하는 시간
        people[i][0], people[i][1]=abs(people[i][0]-stairs[0][0])+abs(people[i][1]-stairs[0][1]), abs(people[i][0]-stairs[1][0])+abs(people[i][1]-stairs[1][1])
    visited=[False for _ in range(num)] #사람 수만큼 visited 배열 생성
    ans=float('inf')
    go(0) #사람마다 1번 또는 2번 계단 어디로 갈지 조합 계산
    print('#{} {}'.format(test_case, ans))