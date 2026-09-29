class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr_max = curr_min = ans = nums[0]
        for i in nums[1:]:
            candidates = (i,curr_max * i ,curr_min * i)
            curr_max = max(candidates)
            curr_min = min(candidates)
            ans = max(ans,curr_max)

        return ans