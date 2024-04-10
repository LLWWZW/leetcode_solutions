class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mp = collections.defaultdict(int) # 用来存放前缀和出现的次数
        mp[0] = 1
        pre_sum = 0
        count = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum - k in mp.keys():
                count += mp[pre_sum - k]
            mp[pre_sum] += 1
        return count