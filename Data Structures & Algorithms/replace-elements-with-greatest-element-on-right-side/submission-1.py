class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Optimal Solution
        n = len(arr)
        rightMax = -1
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            arr[i] = rightMax
            rightMax = max(curr, rightMax)
        return arr

        