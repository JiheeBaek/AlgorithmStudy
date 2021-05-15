T=int(input())
for test_case in range(1, T+1):
    K=int(input())
    mag=[list(map(int, input().strip().split(' '))) for _ in range(4)]
    rotate=[]
    for i in range(K):
        idx, d=list(map(int, input().strip().split(' ')))
        rotate.append([idx-1, d])
    for k in range(K):
        idx, d=rotate[k]
        move=[[idx, d]]
        temp=d
        for i in range(idx+1, 4): #오른쪽 확인
            if mag[i-1][2]!=mag[i][6]:
                temp*=-1
                move.append([i, temp])
            else:
                break
        temp=d
        for i in range(idx-1, -1, -1): #왼쪽 확인
            if mag[i+1][6]!=mag[i][2]:
                temp*=-1
                move.append([i, temp])
            else:
                break
        for i in range(len(move)):
            idx, d=move[i]
            if d==1:
                mag[idx]=[mag[idx][-1]]+mag[idx][:-1]
            else:
                mag[idx]=mag[idx][1:]+[mag[idx][0]]
    ans=0
    for i in range(4):
        ans+=mag[i][0]*2**i
    print('#{} {}'.format(test_case, ans))
