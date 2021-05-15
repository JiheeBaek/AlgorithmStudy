def down(s_info, length): #s_info에는 이 계단에 사람들이 몇분에 도착하는지에 대한 정보, 계단의 길이
    if not s_info: #stairs에 사람이 0명인 경우
        return 0
    elif len(s_info)<4: #이 계단에 오는 사람이 3명 이하인 경우
        return s_info[0]+1+length

    #이 계단에 오는 사람이 4명 이상인 경우
    stairs=[]
    while len(s_info)>1:
        time=s_info.pop()
        stairs=[time]+stairs
        if len(stairs)==3:
            if stairs[-1]+1+length > s_info[-1]+1:
            #계단에 제일 먼저 들어온 사람이 나가는 시간 vs 이번에 오는 사람이 계단에 들어오는 시간
            #이번에 오는 사람이 기다려야하는 경우
                s_info[-1]=stairs[-1]+length
            stairs.pop()
    return s_info[0]+1+length

#조합 계산할 때 한 그룹에 몇 개의 원소가 들어올지 정해지지 않은 경우!!!!
# 1) check를 False로 초기화
# 2) cur이 False일 때, 재귀
# 3) cur이 True일 때, 재귀

def go(cur):
    if cur==p_num:
        global ans
        stairs1, stairs2=[], []
        for i in range(p_num): #1번 또는 2번 계단이라서 true 또는 false로 나눌 수 있는 것
            if check[i]==True: #첫번째 계단
                stairs1.append(people[i][0])
            else: #두번째 계단
                stairs2.append(people[i][1])
        temp=max(down(sorted(stairs1, reverse=True), exits[0][2]), down(sorted(stairs2, reverse=True), exits[1][2]))
        ans=min(temp, ans)
        return
    check[cur]=False
    go(cur+1)
    check[cur]=True
    go(cur+1)

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    matrix=[]
    for _ in range(N):
        matrix.append(list(map(int, input().split(' '))))
    people, exits=[], [] #사람 위치, 출구 위치
    p_num=0 #사람 수
    ans=float('inf')
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==1: #사람이면
                p_num+=1
                people.append([i, j])
            elif matrix[i][j]==0:
                continue
            else: #출구면
                exits.append([i, j, matrix[i][j]]) #출구 위치, 계단 길이
    for i in range(p_num):
        distance1=abs(people[i][0]-exits[0][0])+abs(people[i][1]-exits[0][1])
        distance2=abs(people[i][0]-exits[1][0])+abs(people[i][1]-exits[1][1])
        #이제 people 리스트에는 [distance1, distance2]가 들어감
        #distance = 몇 분 후에 출구에 도착하는가
        people[i][0]=distance1
        people[i][1]=distance2
    #1번 출구/2번 출구로 갈지 모든 조합 계산
    check=[False for _ in range(p_num)]
    go(0)
    print('#{} {}'.format(test_case, ans))