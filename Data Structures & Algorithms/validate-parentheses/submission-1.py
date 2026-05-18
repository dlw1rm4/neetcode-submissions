class Solution:
    def isValid(self, s: str) -> bool:
        hm = {')':'(', '}':'{', ']':'['}
        stk = []

        for c in s:
            if c not in hm:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hm[c]:
                        return False
        return not stk