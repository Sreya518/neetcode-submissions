class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute-force solution: TC - O(N^2) SC - O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+ nums[j] == target:
        #             return [i, j]

        #Better/Optimal Solutions
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        
            

        