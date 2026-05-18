class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = Counter(s)
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        
        return True