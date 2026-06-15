class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Brute-Force Solution
        result = []
        for word in strs:
            placed = False
            for group in result:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    placed = True
                    break
            if not placed:
                result.append([word])
        return result   