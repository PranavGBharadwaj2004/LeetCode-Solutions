from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] stores the minimum number of coins needed to make amount i
        # We initialize with amount + 1, which acts as "infinity" here
        # since the maximum coins needed cannot exceed the amount itself.
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Build up the dp array for all amounts from 1 to 'amount'
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # If the value at dp[amount] is still amount + 1, it means the amount 
        # cannot be formed by any combination of the given coins.
        return dp[amount] if dp[amount] != amount + 1 else -1
