class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin, currMax = 0, 0
        MaxSum, MinSum = nums[0], nums[0]
        total = 0

        for n in nums:
            currMin = min(currMin+n, n)
            currMax = max(currMax+n, n)
            total += n
            MaxSum = max(currMax, MaxSum)
            MinSum = min(currMin, MinSum)
        return max(MaxSum, total-MinSum) if MaxSum>0 else MaxSum

        