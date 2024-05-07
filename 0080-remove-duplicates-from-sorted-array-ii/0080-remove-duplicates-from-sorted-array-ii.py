class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(2,len(nums)):
            if nums[right]==nums[left-1] and nums[right]==nums[left]:
                continue
            left += 1
            nums[left] = nums[right]
        return left+1