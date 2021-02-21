n, k = list(map(int, input().split(' ')))
dp=[0 for _ in range(k+1)]
coin=[]
for _ in range(n):
    coin.append(int(input()))

dp[0]=1
for c in range(n):
    for i in range(coin[c], k+1): #동전 c가  값 i를 만들 때 사용될 수 있는가
        if i-coin[c]>=0:
            dp[i]+=dp[i-coin[c]]

print(dp[k])