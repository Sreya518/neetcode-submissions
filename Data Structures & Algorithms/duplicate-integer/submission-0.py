class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute-Force Solution -  To check with two for loops one with each on of the remaining value in Array
        #TC - O(N^2) AND SC - O(1)
        #BETTER SOLUTION - I can sort the arrays and check of i = i-1
        #TC - O(NlogN) and SC - O(1)
        #Optimal SOLUTION - SET'S 
        #TC - O(N) AND SC - O(N)
        distinct = set()
        for num in nums:
            if num in distinct:
                return True
            distinct.add(num)
        return False