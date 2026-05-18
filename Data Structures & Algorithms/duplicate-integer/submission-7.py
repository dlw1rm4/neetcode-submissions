class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = set()

        for num in nums: 
            if num in hm:
                return True
            hm.add(num)
        return False