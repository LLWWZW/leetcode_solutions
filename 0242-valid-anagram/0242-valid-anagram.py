class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
            if t[i] not in hashmap:
                hashmap[t[i]] = -1
            else:
                hashmap[t[i]] -= 1
        
        for key,val in hashmap.items():
            if val != 0:
                return False
        return True
        