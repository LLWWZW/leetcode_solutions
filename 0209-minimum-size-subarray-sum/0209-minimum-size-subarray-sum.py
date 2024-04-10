class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,1
        res = sum(nums) + 1
        val = 0
        while r <= len(nums): 
            val += nums[r-1]
            while val>=target :
                res = min(res,r-l)
                val -= nums[l]
                l += 1
            r += 1
        if res == sum(nums) + 1:
            return 0
        else:
            return res