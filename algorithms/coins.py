coins = [1,2,5]
amount = 11

def coin_change(coinList, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    print(dp)
    for a in range(1, amount+1):
        for c in coinList:
            if a - c >= 0:
                print(a, end='   ')
                print(a-c)
                print(dp)
                dp[a] = min(dp[a], 1 + dp[a - c])
    print (dp)
    return dp[amount] if dp[amount] != amount + 1 else -1

coin_change(coins, amount)