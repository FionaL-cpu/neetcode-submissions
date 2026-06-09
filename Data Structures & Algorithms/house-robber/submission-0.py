class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [0 for _ in range(len(nums) + 2)]
        # [0,0,...0] 0, 1,3,,,n + 1 
        dp[0] = 0
        dp[1] = 0
        dp[2] = nums[0]# dp[i + 2] = nums[i]
        
        for i in range(1, len(nums)): 
            dp[i + 2] = max(dp[i + 1], nums[i] + dp[i])
        return dp[len(nums) + 1]