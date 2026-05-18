class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            hit = target - n
            if hit in hm:
                return [hm[hit], i]
            hm[n] = i