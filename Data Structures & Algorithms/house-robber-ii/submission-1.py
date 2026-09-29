class Solution:
    def rob(self, nums: List[int]) -> int:
        #consider not stole the first or not stole the last one
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(houses):
            pre, curr = 0,0
            for money in houses:
                pre,curr = curr, max(curr, pre + money)
            return curr
        return max(helper(nums[1:]), helper(nums[:-1]))
