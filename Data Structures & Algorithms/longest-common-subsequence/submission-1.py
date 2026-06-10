class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # m * n matrix

        #dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        row = [0] * (n + 1)

        for r in range(1, m + 1):
            
            newRow = [0] * (n + 1)
            for c in range(1, n + 1): 
                if text1[r - 1] == text2[c - 1]:
                    newRow[c] = row[c - 1] + 1 
                else: 
                    newRow[c] = max(row[c], newRow[c - 1])
            row = newRow 
                
        return row[n]


        