T=int(input())
for test_case in range(1, T+1):
    N, K=list(map(int, input().strip().split(' ')))
    string=input()
    nums=[]
    for i in range(N):
        for j in range(4):
            nums.append(int(string[j:j+N//4], 16))
        string=string[-1]+string[:-1]
    nums=sorted(list(set(nums)), reverse=True)
    print('#{} {}'.format(test_case, nums[K-1]))
