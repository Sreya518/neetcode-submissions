class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l= 0
        curSum = sum(arr[:k])
        for l in range(len(arr)-k+1):
            if curSum/k >= threshold:
                res += 1
            if l + k < len(arr):
                curSum -= arr[l]
                curSum += arr[l+k]
        return res

        
        