from collections import deque

def repair():
    global b_queue, client_check
    for i in range(M):
        if b_check[i][0]!=0:
            b_check[i][0]-=1
        elif b_check[i][0]==0 and b_check[i][1]!=-1:
            b_check[i] = [0, -1]
    while b_queue:
        wait = True
        for i in range(M):
            if b_check[i][0] == 0 and b_check[i][1] == -1:
                wait = False
                b_check[i] = [bi[i]-1, b_queue[0]]
                client_check[b_queue[0]]=True
                b_queue.popleft()
                if i+1==B:
                    B_list.append(b_check[i][1] + 1)
                if not b_queue:
                    break
        if wait:
            break
    return

def recep():
    global a_queue, A_list
    temp = []
    for i in range(N):
        if a_check[i][0]!=0:
            a_check[i][0]-=1
        elif a_check[i][0]==0 and a_check[i][1]!=-1:
            temp.append((i, a_check[i][1]))  # 몇번째 접수 창구에서 받았는지, 고객번호
            a_check[i] = [0, -1]
    while a_queue:
        wait=True
        for i in range(N):
            if a_check[i][0]==0 and a_check[i][1]==-1:
                wait=False
                a_check[i]=[ai[i]-1, a_queue[0]]
                a_queue.popleft()
                if i+1==A:
                    A_list.append(a_check[i][1] + 1)
                if not a_queue:
                    break
        if wait:
            break
    temp=sorted(temp)
    for i in range(len(temp)):
        b_queue.append(temp[i][1])
    return

T=int(input())
for test_case in range(1, T+1):
    N, M, K, A, B=list(map(int, input().split(' ')))
    ai=list(map(int, input().split(' ')))
    bi=list(map(int, input().split(' ')))
    tk=list(map(int, input().split(' ')))
    time=tk[0]
    A_list=[]
    B_list=[]
    a_check=[[0, -1] for _ in range(N)] #종료까지 남은 시간, 몇번째 고객인지 idx
    b_check=[[0, -1] for _ in range(M)]
    a_queue = deque([])
    b_queue = deque([]) #몇번째 접수 창구, 고객 idx
    client_check=[False for _ in range(K)]
    idx=0
    while True:
        while tk:
            if tk[0]==time:
                a_queue.append(idx)#고객의 idx
                tk=tk[1:]
                idx+=1
            else:
                break
        recep()
        repair()
        ####################################################
        '''
        print("현재 시간", time)
        print("접수 창구 상황(남은 시간, 고객 번호-1)", a_check)
        print("a_wait", a_queue)
        print("정비 창구 상황(남은 시간, 고객 번호-1)", b_check)
        print("b_wait", b_queue)
        print('\n')
        '''
        #################################################
        time += 1
        if client_check==[True for _ in range(K)]:
            break
    ans = 0
    for i in range(len(A_list)):
        if A_list[i] in B_list:
            ans+=A_list[i]
    if ans==0:
        ans=-1
    print('#{} {}'.format(test_case, ans))