class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)

        for char in t:
            if char in count_s and count_s[char] > 0:
                count_s[char] -= 1
            else:
                return False
        return True
        