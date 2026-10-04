class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = float('-inf')
        count = 0
        #continue to add untill it equal to 
        for num in nums:
            if count < 0:
                count = 0
            count += num
            max_sum = max(max_sum, count)
        return max_sum
    
#max_sum 2 2 4 4 

        