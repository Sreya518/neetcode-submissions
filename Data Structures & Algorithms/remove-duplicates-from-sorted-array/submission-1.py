class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #TC - O(N)
        #SC - O(1)
        index = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
                       