class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        for i in count:
            if i!=0:
                return False
        return True

        #Bruter force
        # if len(s) != len(t):
        #     return False

        # t = list(t)
        
        # for c in s:
        #     if c not in t:
        #         return false
        #     t.remove(c)
        # return True


