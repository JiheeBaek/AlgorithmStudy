def check(temp):
    cnt = 1
    prev = temp[0]
    flag=True
    installed=[False for _ in range(N)]
    for j in range(1, N):
        if temp[j]==prev:
            if installed[j-1]:
                cnt=1
                prev=temp[j]
            else:
                cnt+=1
                prev=temp[j]
        elif prev - temp[j] == -1:  # _-
            if installed[j-1]==False and cnt>=X:
                #현재 위치 앞쪽에 활주로 설치
                cnt=1
                prev=temp[j]
            else:
                flag=False
                break
        elif prev-temp[j]==1: #-_
            local_prev = temp[j]
            local_cnt = 1
            for x in range(1, X):
                if j + x == N:
                    flag = False
                    break
                if local_prev == temp[j + x]:
                    local_cnt += 1
                else:
                    break
            if installed[j]==False and local_cnt >= X:  # 경사로 설치
                for x in range(X):
                    installed[j + x] = True
                cnt = 1
                prev = temp[j]
            else:
                flag = False
                break
        else:
            flag=False
            break
    #print(flag,temp, installed)
    if flag:
        return 1
    else:
        return 0

T=int(input())
for test_case in range(1, T+1):
    N, X=list(map(int, input().strip().split(' ')))
    matrix=[]
    for _ in range(N):
        matrix.append(list(map(int, input().strip().split(' '))))
    ans=0
    #1. 행에 따라 확인
    for i in range(N):
        temp=[]
        for j in range(N):
            temp.append(matrix[i][j])
        ans+=check(temp)

    #2. 열에 따라 확인
    for i in range(N):
        temp=[]
        for j in range(N):
            temp.append(matrix[j][i])
        ans+=check(temp)
    print('#{} {}'.format(test_case, ans))