class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_(begin,res):
            tmp = ""
            for i in range(k//2):
                tmp = res[begin+i]
                res[begin+i] = res[begin+k-i-1]
                res[begin+k-i-1] = tmp
            return res
        res = list(s)
        count = len(s) // (2*k)
        for i in range(count):
            res = reverse_(i*2*k,res)
        if k <= len(s)-count*2*k <2*k:
            res = reverse_(count*2*k,res)
        elif 0 < len(s)-count*2*k <k:
            tmp = ""
            end = len(s)
            begin = count*2*k
            for i in range((end-begin+1)//2):
                tmp = res[begin+i]
                res[begin+i] = res[end-i-1]
                res[end-i-1] = tmp
        
        return ''.join(res)