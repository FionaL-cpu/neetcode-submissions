class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0 

        for i in range(amount + 1): #0, 1, 2,,, 11, 12
            for c in coins: 
                if (i - c) >= 0:
                    dp[i] = min(dp[i - c] + 1, dp[i])

        if dp[-1] == float("inf"):
            return -1
        else: 
            return dp[-1]

                    
            