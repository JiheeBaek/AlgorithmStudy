def check(A, B):
    for j in range(W): #각 세로줄에 대하여 검사
        if 0 in A:
            prev=0 #A : A 약품을 처리할 가로줄 index
        elif 0 in B:
            prev=1 #B : B 약품을 처리할 가로줄 index
        else:
            prev=matrix[0][j] #약품 처리 안하는 경우 자기 자신 값
        cnt=1
        for i in range(1, D):
            if i in A:
                cur=0
            elif i in B:
                cur=1
            else:
                cur = matrix[i][j]
            if prev==cur:#이전 칸과 같은 성분인지 확인
                cnt+=1
            else:
                cnt=1
            prev=cur
            if cnt==K: #한 번이라도 K개의 같은 성분이 연달아 나오면, 다음 세로줄 검사
                break
        if cnt<K:
            return False #한 열이라도 K보다 작으면 탈락
    return True #테스트 통과

def ab_go(cur): #go 함수에서 몇 번째 index 가로줄에 약품을 처리할지 골랐다면 그 index에 A/B 중 어느 약품을 처리할지
    global flag, ab_visited, ab_change
    if cur==len(ab_visited):
        A=[]  #특성 A : 0
        B=[]  #특성 B : 1
        for i in range(len(ab_visited)):
            if ab_visited[i]:
                A.append(ab_change[i])
            else:
                B.append(ab_change[i])
        if check(A, B):
            flag=True
        return
    ab_visited[cur]=False
    ab_go(cur+1)
    ab_visited[cur]=True
    ab_go(cur+1)

def go(cur):
    global ans, flag, ab_visited, ab_change
    if cur==D:
        ab_change=[] #몇 번째 행에 약품 처리를 할지 그 index가 들어감
        cnt=0
        flag=False
        for i in range(D):
            if visited[i]:
                cnt+=1
                ab_change.append(i)
        if cnt>ans: #여기가 실행 시간 결정에 중요한 부분!!
            return
        ab_visited=[False for _ in range(cnt)]
        ab_go(0)
        if flag:
            ans=min(ans, cnt)
        return
    visited[cur]=False
    go(cur+1)
    visited[cur]=True
    go(cur+1)

T=int(input())
for test_case in range(1, T+1):
    D, W, K = list(map(int, input().split(' ')))
    matrix=[list(map(int, input().split(' '))) for _ in range(D)]
    visited=[False for _ in range(D)] #몇 번째 layer에 약품 처리를 할지
    ab_visited=[] #몇 번째 layer에 약품 처리할지 정한 후, a와 b 중 어떤 약품을 할지
    ab_change=[]
    flag=False
    ans = float('inf')
    if check([], []):
        print('#{} {}'.format(test_case, 0))
        continue
    go(0)
    print('#{} {}'.format(test_case, ans))