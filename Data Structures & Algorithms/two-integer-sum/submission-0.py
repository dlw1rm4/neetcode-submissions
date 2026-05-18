class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            needed_num = target - n
            if needed_num in hm:
                return [hm[needed_num], i]
            hm[n] = i