class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set(nums)

        max_len = 0
        for n in nums:
            if n - 1 in contains: continue
            cur, cur_len = n, 0
            while cur in contains:
                cur += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len