class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Brute-Force Solution
        for i in range(len(arr)- 1):
            maxnum = arr[i+1]
            for j in range(i+1, len(arr)):
                maxnum = max(maxnum, arr[j])
            arr[i] = maxnum
        arr[-1] = -1
        return arr

        