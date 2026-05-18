class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hm:
                return [hm[complement], i]
            hm[num] = i
        return [0,0]