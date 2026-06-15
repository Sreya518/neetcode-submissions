class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcnt, cnt = 0,0
        for num in nums:
            if num != 1:
                cnt = 0
            else:
                cnt += 1
                maxcnt = max(maxcnt, cnt)
        return maxcnt
        