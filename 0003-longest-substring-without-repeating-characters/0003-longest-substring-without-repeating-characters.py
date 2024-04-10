class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        l = 0
        r = 0
        window = collections.defaultdict(int)
        while r <= len(s)-1:
            window[s[r]] += 1
            r += 1

                res = max(res,r-l)
            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1
            
            
        return res