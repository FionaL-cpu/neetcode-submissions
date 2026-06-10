class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # m * n matrix

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]: # equal: upper left + 1
                    dp[row][col] =dp[row - 1][col - 1] + 1 
                
                else: # left or upper
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
        return dp[m][n]


        