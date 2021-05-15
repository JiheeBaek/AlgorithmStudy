T=int(input())
for test_case in range(1, T+1):
    K=int(input()) #몇 번 회전 시키는지
    magnetic=[] #4개 자석에 대한 정보
    for _ in range(4):
        magnetic.append(list(map(int, input().strip().split(' '))))
    turn=[] #K개 회전 정보
    for _ in range(K):
        turn.append(list(map(int, input().strip().split(' '))))

    for k in range(K):
        num, dir=turn[k]
        turn_mag=[]
        if num==1:
            #2번 비교, -> 2번 다르면 3번 비교 -> 3번 다르면 4번
            if magnetic[0][2] != magnetic[1][6]:  # 1번과 2번 자석이 다르면
                if magnetic[1][2] != magnetic[2][6]:  # 2번과 3번 자석이 다르면
                    if magnetic[2][2] != magnetic[3][6]:  # 3번과 4번 자석이 다르면
                        if dir==1: #4번은 반시계
                            magnetic[3] = magnetic[3][1:] + [magnetic[3][0]]
                        else: #4번은 시계
                            magnetic[3] = [magnetic[3][-1]] + magnetic[3][:-1]
                    if dir==1: #3번은 시계
                        magnetic[2] = [magnetic[2][-1]] + magnetic[2][:-1]
                    else: #3번은 반시계
                        magnetic[2] = magnetic[2][1:] + [magnetic[2][0]]
                if dir == 1: #2번은 반시계
                    magnetic[1] = magnetic[1][1:] + [magnetic[1][0]]
                else: #2번은 시계
                    magnetic[1] = [magnetic[1][-1]] + magnetic[1][:-1]
            if dir == 1: #1번은 시계
                magnetic[0] = [magnetic[0][-1]] + magnetic[0][:-1]
            else: #1번은 반시계
                magnetic[0] = magnetic[0][1:] + [magnetic[0][0]]

        elif num==2:
            #1번, 3번 비교 -> 3번 다르면 4번
            temp=magnetic[1][6] #1번을 마지막에 비교할 것
            if magnetic[1][2] != magnetic[2][6]:  # 2번과 3번 자석이 다르면
                if magnetic[2][2] != magnetic[3][6]:  # 3번과 4번 자석이 다르면
                    if dir == 1:  # 4번은 시계
                        magnetic[3] = [magnetic[3][-1]] + magnetic[3][:-1]
                    else:  # 4번은 반시계
                        magnetic[3] = magnetic[3][1:] + [magnetic[3][0]]
                if dir == 1: #3번은 반시계
                    magnetic[2] = magnetic[2][1:] + [magnetic[2][0]]
                else: #3번은 시계
                    magnetic[2] = [magnetic[2][-1]] + magnetic[2][:-1]
            if dir == 1:  # 2번은 시계
                magnetic[1] = [magnetic[1][-1]] + magnetic[1][:-1]
            else:  # 2번은 반시계
                magnetic[1] = magnetic[1][1:] + [magnetic[1][0]]

            if magnetic[0][2]!=temp: #1번과 2번 자석이 다르면
                if dir == 1: #1번은 반시계
                    magnetic[0] = magnetic[0][1:] + [magnetic[0][0]]
                else: #3번은 시계
                    magnetic[0] = [magnetic[0][-1]] + magnetic[0][:-1]

        elif num==3:
            #2번, 4번 비교 -> 2번 다르면 1번
            temp = magnetic[2][2]  # 4번을 마지막에 비교할 것
            if magnetic[1][2] != magnetic[2][6]:  # 2번과 3번 자석이 다르면
                if magnetic[0][2] != magnetic[1][6]:  # 1번과 2번 자석이 다르면
                    if dir == 1:  # 1번은 시계
                        magnetic[0] = [magnetic[0][-1]] + magnetic[0][:-1]
                    else:  # 1번은 반시계
                        magnetic[0] = magnetic[0][1:] + [magnetic[0][0]]
                if dir == 1:  # 2번은 반시계
                    magnetic[1] = magnetic[1][1:] + [magnetic[1][0]]
                else:  # 2번은 시계
                    magnetic[1] = [magnetic[1][-1]] + magnetic[1][:-1]
            if dir == 1:  # 3번은 시계
                magnetic[2] = [magnetic[2][-1]] + magnetic[2][:-1]
            else:  # 3번은 반시계
                magnetic[2] = magnetic[2][1:] + [magnetic[2][0]]

            if magnetic[3][6] != temp:  # 3번과 4번 자석이 다르면
                if dir == 1:  # 4번은 반시계
                    magnetic[3] = magnetic[3][1:] + [magnetic[3][0]]
                else:  # 4번은 시계
                    magnetic[3] = [magnetic[3][-1]] + magnetic[3][:-1]
        else:
            #3번 비교 -> 3번 다르면 2번 비교 -> 2번 다르면 1번 비교
            if magnetic[2][2] != magnetic[3][6]:  # 3번과 4번 자석이 다르면
                if magnetic[1][2] != magnetic[2][6]:  # 2번과 3번 자석이 다르면
                    if magnetic[0][2] != magnetic[1][6]:  # 1번과 2번 자석이 다르면
                        if dir==1: #1번은 반시계
                            magnetic[0] = magnetic[0][1:] + [magnetic[0][0]]
                        else: #1번은 시계
                            magnetic[0] = [magnetic[0][-1]] + magnetic[0][:-1]
                    if dir==1: #2번은 시계
                        magnetic[1] = [magnetic[1][-1]] + magnetic[1][:-1]
                    else: #2번은 반시계
                        magnetic[1] = magnetic[1][1:] + [magnetic[1][0]]
                if dir == 1: #3번은 반시계
                    magnetic[2] = magnetic[2][1:] + [magnetic[2][0]]
                else: #2번은 시계
                    magnetic[2] = [magnetic[2][-1]] + magnetic[2][:-1]
            if dir == 1: #4번은 시계
                magnetic[3] = [magnetic[3][-1]] + magnetic[3][:-1]
            else: #4번은 반시계
                magnetic[3] = magnetic[3][1:] + [magnetic[3][0]]
        #for i in range(4):
        #    print(magnetic[i])
        #print('\n')

    ans=0
    for i in range(4):
        if magnetic[i][0]==0: #N이면
            continue
        else:
            ans+=2**i
    print("#{} {}".format(test_case, ans))
