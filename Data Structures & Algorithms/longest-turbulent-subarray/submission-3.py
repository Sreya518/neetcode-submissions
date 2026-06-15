class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #[2,4,3,2,2,5,1,4]
        l = 0
        r = 1
        length = 1
        prev = ""

        while r < len(arr):
            if arr[r-1] < arr[r] and prev!= "<":
                length = max(r-l+1, length)
                r += 1
                prev = "<"
            elif arr[r-1] > arr[r] and prev!= ">":
                length = max(r-l+1, length)
                r += 1
                prev = ">"
            else:
                r = r+1 if arr[r-1] == arr[r] else r
                l = r-1
                prev = ""
        return length
