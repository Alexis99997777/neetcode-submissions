class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greddy
        #dont need to care how to jump just need to care about how far it can jump
        farthest = 0
        i = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True

            