class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_seen = set()

        for n in nums:
            if n in nums_seen:
                return True
            nums_seen.add(n)
        return False
        