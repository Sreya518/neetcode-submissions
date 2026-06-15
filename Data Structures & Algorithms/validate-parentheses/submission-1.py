class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pairs:
                if ans and ans[-1] == pairs[c]:
                    ans.pop()
                else:
                    return False
            else:
                ans.append(c)
        return True if not ans else False

            


        