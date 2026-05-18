class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            desired_val = target - n
            if desired_val in hm:
                return [hm[desired_val], i]
            hm[n] = i
        