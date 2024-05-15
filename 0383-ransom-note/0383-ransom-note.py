class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = dict()
        for mag in magazine:
            if mag not in hashmap:
                hashmap[mag] = 1
            else:
                hashmap[mag] += 1
        
        for rn in ransomNote:
            if rn not in hashmap.keys():
                return False
            hashmap[rn] -= 1
            if hashmap[rn] < 0:
                return False
        return True