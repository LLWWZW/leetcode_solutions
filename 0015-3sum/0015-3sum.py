class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)):
            move = i
            if nums[move] > 0:
                return res
            
            if move>0 and nums[move] == nums[move-1]:
                continue

            left,right = move+1, len(nums)-1
            tmp = 0 - nums[move]
            while left<right:
                if tmp == (nums[left] + nums[right]):
                    res.append([nums[move],nums[left],nums[right]])

                    while left<right and nums[left] == nums[left + 1]:
                        left += 1
                    while left<right and nums[right] == nums[right -1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif  tmp < (nums[left] + nums[right]):
                    right -= 1
                else:
                    left += 1
        return res