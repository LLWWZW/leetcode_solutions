class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        boardline = -1
        # find the boardline 
        for i in range(len(nums)):
            if nums[i] < 0:
                boardline = i
        result = []
        to_left = boardline
        to_right = boardline + 1
        while to_left >= 0 or to_right<= len(nums)-1:
            if to_left < 0 and to_right <= len(nums)-1:
                result.append(nums[to_right]**2)
                to_right += 1
            elif to_left >= 0 and to_right > len(nums)-1:
                result.append(nums[to_left]**2)
                to_left -= 1
            else:
                if nums[to_left]**2 > nums[to_right]**2:
                    result.append(nums[to_right]**2)
                    to_right += 1
                else:
                    result.append(nums[to_left]**2)
                    to_left -= 1
        return result